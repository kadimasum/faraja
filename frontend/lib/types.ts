export type ProjectStatus =
  | "planned"
  | "in_progress"
  | "delayed"
  | "completed"
  | "cancelled";

export interface Project {
  id: number;
  name: string;
  description: string;
  county: string;
  constituency?: string | null;
  budget_allocated: number;
  budget_spent: number;
  start_date: string;
  target_end_date: string;
  status: ProjectStatus;
  implementing_agency: string;
  lead_politician: string;
  created_at: string;
  updated_at: string;
}

export interface CreateProjectPayload {
  name: string;
  description: string;
  county: string;
  constituency?: string;
  budget_allocated: number;
  budget_spent: number;
  start_date: string;
  target_end_date: string;
  status: ProjectStatus;
  implementing_agency: string;
  lead_politician: string;
}
