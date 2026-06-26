# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T05:37:30.772042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.084` n `12`; crypto_alt avg `0.4435` n `228`; crypto_major avg `0.4054` n `8`; equity avg `0.2745` n `86`; fx avg `-0.0189` n `6`; index avg `0.078` n `23`; metal avg `0.1253` n `20`; unknown avg `1.9486` n `765`
- 1h: commodity avg `0.1016` n `12`; crypto_alt avg `0.2986` n `228`; crypto_major avg `0.2164` n `8`; equity avg `0.4216` n `86`; fx avg `-0.0229` n `6`; index avg `0.1479` n `23`; metal avg `0.1823` n `20`; unknown avg `1.2498` n `765`
- 4h: commodity avg `-0.0976` n `12`; crypto_alt avg `0.2893` n `228`; crypto_major avg `0.5775` n `8`; equity avg `-0.8443` n `86`; fx avg `-0.0435` n `6`; index avg `-0.1905` n `23`; metal avg `-0.1368` n `20`; unknown avg `0.5059` n `749`
- 24h: commodity avg `0.3789` n `12`; crypto_alt avg `-2.6474` n `228`; crypto_major avg `-2.5165` n `8`; equity avg `-3.9861` n `86`; fx avg `0.063` n `6`; index avg `-0.6176` n `23`; metal avg `0.1133` n `20`; unknown avg `0.7068` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2007`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
