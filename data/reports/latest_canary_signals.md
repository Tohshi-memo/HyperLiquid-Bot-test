# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T19:22:27.213687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `0.085` n `236`; crypto_major avg `0.1005` n `8`; equity avg `-0.0164` n `151`; fx avg `0.0028` n `6`; index avg `-0.0015` n `26`; metal avg `0.0041` n `20`; unknown avg `2.7471` n `1193`
- 1h: commodity avg `-0.0052` n `13`; crypto_alt avg `0.2367` n `236`; crypto_major avg `0.0473` n `8`; equity avg `0.0961` n `151`; fx avg `0.0072` n `6`; index avg `0.0294` n `26`; metal avg `0.0032` n `20`; unknown avg `6.2459` n `1183`
- 4h: commodity avg `0.0071` n `13`; crypto_alt avg `0.0604` n `236`; crypto_major avg `-0.0676` n `8`; equity avg `0.0156` n `151`; fx avg `-0.0358` n `6`; index avg `-0.0187` n `26`; metal avg `-0.0178` n `20`; unknown avg `0.7786` n `1137`
- 24h: commodity avg `0.0512` n `13`; crypto_alt avg `-0.8304` n `236`; crypto_major avg `-0.0708` n `8`; equity avg `-0.2859` n `151`; fx avg `-0.0204` n `6`; index avg `-0.0433` n `26`; metal avg `-0.0088` n `20`; unknown avg `4.0313` n `1011`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1723`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1477`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
