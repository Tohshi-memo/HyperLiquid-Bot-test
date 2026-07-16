# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T22:43:38.244151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `-0.3661` n `230`; crypto_major avg `-0.2981` n `8`; equity avg `-0.0647` n `94`; fx avg `0.0005` n `6`; index avg `-0.0143` n `25`; metal avg `-0.0148` n `20`; unknown avg `-0.1283` n `768`
- 1h: commodity avg `0.031` n `12`; crypto_alt avg `-0.598` n `230`; crypto_major avg `-0.5027` n `8`; equity avg `-0.2619` n `94`; fx avg `-0.0026` n `6`; index avg `-0.0569` n `25`; metal avg `-0.0547` n `20`; unknown avg `-0.2275` n `768`
- 4h: commodity avg `0.2137` n `12`; crypto_alt avg `-0.3974` n `230`; crypto_major avg `-0.2633` n `8`; equity avg `-0.4539` n `94`; fx avg `-0.0056` n `6`; index avg `-0.0513` n `25`; metal avg `-0.0249` n `20`; unknown avg `-0.3672` n `768`
- 24h: commodity avg `-0.1911` n `12`; crypto_alt avg `-1.541` n `230`; crypto_major avg `-2.5016` n `8`; equity avg `-3.7931` n `94`; fx avg `-0.1752` n `6`; index avg `-0.5241` n `25`; metal avg `-0.8785` n `20`; unknown avg `-0.4894` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
