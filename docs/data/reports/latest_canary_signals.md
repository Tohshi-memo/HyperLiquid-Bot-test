# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T20:45:19.305639+00:00`
- Correlation status: `ready`
- Asset price records: `202`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3645` n `7`; crypto_alt avg `0.0048` n `223`; crypto_major avg `0.0912` n `7`; equity avg `0.0418` n `42`; fx avg `-0.0109` n `4`; index avg `0.0388` n `9`; metal avg `0.0227` n `7`; unknown avg `-0.0576` n `314`
- 1h: commodity avg `-0.3042` n `7`; crypto_alt avg `0.0936` n `223`; crypto_major avg `0.1185` n `7`; equity avg `0.0087` n `42`; fx avg `-0.0101` n `4`; index avg `0.0378` n `9`; metal avg `-0.0078` n `7`; unknown avg `-0.0691` n `314`
- 4h: commodity avg `0.0969` n `7`; crypto_alt avg `0.5465` n `223`; crypto_major avg `0.3506` n `7`; equity avg `0.1632` n `42`; fx avg `-0.0262` n `4`; index avg `0.0489` n `9`; metal avg `0.0879` n `7`; unknown avg `0.0203` n `313`
- 24h: commodity avg `-0.3849` n `7`; crypto_alt avg `0.0934` n `223`; crypto_major avg `0.3753` n `7`; equity avg `0.2876` n `42`; fx avg `0.0496` n `4`; index avg `0.095` n `9`; metal avg `0.4623` n `7`; unknown avg `0.04` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3989`, n `198`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3821`, n `194`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3812`, n `198`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3749`, n `194`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3688`, n `198`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.356`, n `198`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3365`, n `198`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3184`, n `198`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3063`, n `198`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2548`, n `194`, moderate_sample_signal
