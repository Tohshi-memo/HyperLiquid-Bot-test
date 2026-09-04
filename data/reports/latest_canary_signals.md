# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T06:07:25.123540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `0.0969` n `232`; crypto_major avg `0.1949` n `8`; equity avg `0.0211` n `133`; fx avg `-0.01` n `6`; index avg `-0.004` n `26`; metal avg `0.0309` n `20`; unknown avg `0.2385` n `757`
- 1h: commodity avg `0.0229` n `12`; crypto_alt avg `-0.4546` n `232`; crypto_major avg `-0.231` n `8`; equity avg `-0.0998` n `133`; fx avg `-0.0239` n `6`; index avg `0.0016` n `26`; metal avg `-0.0182` n `20`; unknown avg `1.5759` n `757`
- 4h: commodity avg `-0.0405` n `12`; crypto_alt avg `-0.5239` n `232`; crypto_major avg `0.0249` n `8`; equity avg `0.1938` n `133`; fx avg `-0.0279` n `6`; index avg `0.0818` n `26`; metal avg `-0.1062` n `20`; unknown avg `1.1597` n `757`
- 24h: commodity avg `0.0334` n `12`; crypto_alt avg `1.8642` n `232`; crypto_major avg `3.9911` n `8`; equity avg `1.7743` n `133`; fx avg `-0.0777` n `6`; index avg `0.302` n `26`; metal avg `0.4293` n `20`; unknown avg `2.4515` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
