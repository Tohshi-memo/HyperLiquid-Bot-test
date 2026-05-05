# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T00:30:24.483384+00:00`
- Correlation status: `ready`
- Asset price records: `312`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `7`; crypto_alt avg `-0.0876` n `223`; crypto_major avg `-0.0468` n `7`; equity avg `0.0292` n `47`; fx avg `-0.0046` n `4`; index avg `-0.0199` n `6`; metal avg `-0.0852` n `7`; unknown avg `0.0132` n `312`
- 1h: commodity avg `-0.0573` n `7`; crypto_alt avg `-0.0767` n `223`; crypto_major avg `-0.1044` n `7`; equity avg `0.094` n `47`; fx avg `-0.0096` n `4`; index avg `-0.0054` n `6`; metal avg `0.0051` n `7`; unknown avg `-0.0408` n `312`
- 4h: commodity avg `0.0019` n `7`; crypto_alt avg `-0.005` n `223`; crypto_major avg `-0.01` n `7`; equity avg `0.066` n `47`; fx avg `-0.0123` n `4`; index avg `-0.1906` n `6`; metal avg `0.0088` n `7`; unknown avg `-0.1612` n `312`
- 24h: commodity avg `1.1793` n `7`; crypto_alt avg `2.3507` n `223`; crypto_major avg `1.3703` n `7`; equity avg `-0.3409` n `47`; fx avg `-0.0308` n `4`; index avg `-0.018` n `6`; metal avg `-2.0709` n `7`; unknown avg `-1.1934` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2355`, n `308`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2296`, n `308`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1827`, n `304`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1803`, n `304`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1499`, n `308`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1475`, n `308`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.142`, n `308`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `308`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `304`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.12`, n `308`, weak_sample_signal
