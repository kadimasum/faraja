"use client";

import { FormEvent, useState } from "react";

import { createProject } from "@/lib/api";
import { CreateProjectPayload, ProjectStatus } from "@/lib/types";

const initialState: CreateProjectPayload = {
  name: "",
  description: "",
  county: "",
  constituency: "",
  budget_allocated: 0,
  budget_spent: 0,
  start_date: "",
  target_end_date: "",
  status: "planned",
  implementing_agency: "",
  lead_politician: ""
};

const statuses: ProjectStatus[] = [
  "planned",
  "in_progress",
  "delayed",
  "completed",
  "cancelled"
];

export function ProjectForm() {
  const [form, setForm] = useState<CreateProjectPayload>(initialState);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setSubmitting(true);
    setError(null);

    try {
      await createProject(form);
      setForm(initialState);
      window.location.reload();
    } catch {
      setError("Could not save project. Please try again.");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form className="form" onSubmit={onSubmit}>
      <div className="field">
        <label>Project Name</label>
        <input
          required
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
        />
      </div>

      <div className="field">
        <label>Description</label>
        <textarea
          required
          rows={3}
          value={form.description}
          onChange={(e) => setForm({ ...form, description: e.target.value })}
        />
      </div>

      <div className="grid two">
        <div className="field">
          <label>County</label>
          <input
            required
            value={form.county}
            onChange={(e) => setForm({ ...form, county: e.target.value })}
          />
        </div>
        <div className="field">
          <label>Constituency</label>
          <input
            value={form.constituency}
            onChange={(e) => setForm({ ...form, constituency: e.target.value })}
          />
        </div>
      </div>

      <div className="grid two">
        <div className="field">
          <label>Budget Allocated</label>
          <input
            required
            type="number"
            min="0"
            value={form.budget_allocated}
            onChange={(e) =>
              setForm({ ...form, budget_allocated: Number(e.target.value) })
            }
          />
        </div>
        <div className="field">
          <label>Budget Spent</label>
          <input
            required
            type="number"
            min="0"
            value={form.budget_spent}
            onChange={(e) =>
              setForm({ ...form, budget_spent: Number(e.target.value) })
            }
          />
        </div>
      </div>

      <div className="grid two">
        <div className="field">
          <label>Start Date</label>
          <input
            required
            type="date"
            value={form.start_date}
            onChange={(e) => setForm({ ...form, start_date: e.target.value })}
          />
        </div>
        <div className="field">
          <label>Target End Date</label>
          <input
            required
            type="date"
            value={form.target_end_date}
            onChange={(e) =>
              setForm({ ...form, target_end_date: e.target.value })
            }
          />
        </div>
      </div>

      <div className="grid two">
        <div className="field">
          <label>Status</label>
          <select
            value={form.status}
            onChange={(e) =>
              setForm({ ...form, status: e.target.value as ProjectStatus })
            }
          >
            {statuses.map((status) => (
              <option key={status} value={status}>
                {status}
              </option>
            ))}
          </select>
        </div>
        <div className="field">
          <label>Implementing Agency</label>
          <input
            required
            value={form.implementing_agency}
            onChange={(e) =>
              setForm({ ...form, implementing_agency: e.target.value })
            }
          />
        </div>
      </div>

      <div className="field">
        <label>Lead Politician</label>
        <input
          required
          value={form.lead_politician}
          onChange={(e) => setForm({ ...form, lead_politician: e.target.value })}
        />
      </div>

      {error && <p style={{ color: "var(--danger)", margin: 0 }}>{error}</p>}

      <button type="submit" disabled={submitting}>
        {submitting ? "Saving..." : "Save Project"}
      </button>
    </form>
  );
}
