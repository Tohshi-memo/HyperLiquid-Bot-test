# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T06:37:30.051499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0232` n `12`; crypto_alt avg `-0.3259` n `228`; crypto_major avg `-0.3747` n `8`; equity avg `-0.0426` n `88`; fx avg `0.013` n `6`; index avg `-0.015` n `23`; metal avg `-0.0583` n `20`; unknown avg `0.0654` n `765`
- 1h: commodity avg `-0.1166` n `12`; crypto_alt avg `-0.6788` n `228`; crypto_major avg `-0.8818` n `8`; equity avg `-0.1961` n `88`; fx avg `0.0581` n `6`; index avg `-0.0385` n `23`; metal avg `-0.141` n `20`; unknown avg `11.7486` n `745`
- 4h: commodity avg `-0.1438` n `12`; crypto_alt avg `-0.0014` n `228`; crypto_major avg `-0.641` n `8`; equity avg `0.0414` n `88`; fx avg `0.0004` n `6`; index avg `0.0053` n `23`; metal avg `-0.2673` n `20`; unknown avg `0.0153` n `745`
- 24h: commodity avg `-0.0134` n `12`; crypto_alt avg `-1.1441` n `228`; crypto_major avg `-1.0009` n `8`; equity avg `0.3967` n `88`; fx avg `0.1272` n `6`; index avg `-0.0419` n `23`; metal avg `-0.9482` n `20`; unknown avg `-0.2206` n `745`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
