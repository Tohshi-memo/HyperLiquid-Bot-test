# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T08:37:25.998100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `0.4589` n `232`; crypto_major avg `0.2806` n `8`; equity avg `0.0635` n `134`; fx avg `0.005` n `6`; index avg `0.0005` n `26`; metal avg `0.0369` n `20`; unknown avg `1.4289` n `789`
- 1h: commodity avg `0.0283` n `12`; crypto_alt avg `-0.0803` n `232`; crypto_major avg `-0.0332` n `8`; equity avg `-0.4273` n `134`; fx avg `0.0062` n `6`; index avg `-0.0727` n `26`; metal avg `-0.0397` n `20`; unknown avg `2.5522` n `787`
- 4h: commodity avg `0.2905` n `12`; crypto_alt avg `0.0558` n `232`; crypto_major avg `0.0064` n `8`; equity avg `-1.2405` n `134`; fx avg `0.0485` n `6`; index avg `-0.3121` n `26`; metal avg `-0.2758` n `20`; unknown avg `0.5343` n `747`
- 24h: commodity avg `0.6383` n `12`; crypto_alt avg `0.7695` n `232`; crypto_major avg `-0.6389` n `8`; equity avg `-0.6724` n `134`; fx avg `-0.0666` n `6`; index avg `-0.1793` n `26`; metal avg `-0.0681` n `20`; unknown avg `7508.3802` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
