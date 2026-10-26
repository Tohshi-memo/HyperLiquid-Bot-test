# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T09:07:31.761746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0444` n `13`; crypto_alt avg `-0.3258` n `237`; crypto_major avg `-0.2343` n `8`; equity avg `0.0248` n `152`; fx avg `0.0054` n `6`; index avg `0.0172` n `26`; metal avg `-0.0218` n `20`; unknown avg `-0.1105` n `1238`
- 1h: commodity avg `-0.0358` n `13`; crypto_alt avg `0.8714` n `237`; crypto_major avg `0.5705` n `8`; equity avg `0.4678` n `152`; fx avg `0.0092` n `6`; index avg `0.1037` n `26`; metal avg `0.0151` n `20`; unknown avg `17.4007` n `1206`
- 4h: commodity avg `0.0789` n `13`; crypto_alt avg `-0.0474` n `237`; crypto_major avg `-0.0278` n `8`; equity avg `-0.2661` n `152`; fx avg `0.0146` n `6`; index avg `-0.0192` n `26`; metal avg `-0.0505` n `20`; unknown avg `18.1511` n `1126`
- 24h: commodity avg `-0.5078` n `13`; crypto_alt avg `0.4985` n `237`; crypto_major avg `0.0827` n `8`; equity avg `-0.2294` n `152`; fx avg `0.0384` n `6`; index avg `0.0464` n `26`; metal avg `0.1785` n `20`; unknown avg `-0.3216` n `953`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2544`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2013`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
