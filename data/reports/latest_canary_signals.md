# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T05:07:30.117135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0397` n `12`; crypto_alt avg `-0.3711` n `234`; crypto_major avg `-0.2323` n `8`; equity avg `-0.1271` n `140`; fx avg `-0.0053` n `6`; index avg `-0.016` n `26`; metal avg `-0.0427` n `20`; unknown avg `-0.0092` n `942`
- 1h: commodity avg `0.06` n `12`; crypto_alt avg `-0.0249` n `234`; crypto_major avg `0.068` n `8`; equity avg `-0.0697` n `140`; fx avg `0.0096` n `6`; index avg `-0.0035` n `26`; metal avg `0.011` n `20`; unknown avg `-0.3887` n `942`
- 4h: commodity avg `0.0704` n `12`; crypto_alt avg `0.1815` n `234`; crypto_major avg `-0.723` n `8`; equity avg `-0.294` n `140`; fx avg `-0.0262` n `6`; index avg `0.0054` n `26`; metal avg `-0.1663` n `20`; unknown avg `42.8884` n `936`
- 24h: commodity avg `-0.5588` n `12`; crypto_alt avg `3.3018` n `234`; crypto_major avg `2.3094` n `8`; equity avg `0.9857` n `140`; fx avg `-0.003` n `6`; index avg `0.2085` n `26`; metal avg `0.0064` n `20`; unknown avg `4.1923` n `763`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
