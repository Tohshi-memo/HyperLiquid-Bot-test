# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T01:22:27.284090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0397` n `13`; crypto_alt avg `-0.0835` n `236`; crypto_major avg `-0.0282` n `8`; equity avg `-0.0319` n `151`; fx avg `0.0` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0023` n `20`; unknown avg `-0.0622` n `1193`
- 1h: commodity avg `-0.0684` n `13`; crypto_alt avg `-0.1787` n `236`; crypto_major avg `-0.1627` n `8`; equity avg `0.1791` n `151`; fx avg `-0.0087` n `6`; index avg `0.0049` n `26`; metal avg `-0.0162` n `20`; unknown avg `1.6732` n `1191`
- 4h: commodity avg `0.0949` n `13`; crypto_alt avg `-0.0984` n `236`; crypto_major avg `-0.2642` n `8`; equity avg `-0.0409` n `151`; fx avg `-0.0022` n `6`; index avg `-0.0243` n `26`; metal avg `-0.0092` n `20`; unknown avg `1.1439` n `1183`
- 24h: commodity avg `0.5688` n `13`; crypto_alt avg `-1.5391` n `236`; crypto_major avg `-1.2275` n `8`; equity avg `-3.7795` n `151`; fx avg `-0.0428` n `6`; index avg `-0.6278` n `26`; metal avg `-0.0299` n `20`; unknown avg `40.261` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1702`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1169`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1135`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0915`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0765`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
