# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T15:22:40.914407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0381` n `13`; crypto_alt avg `0.1518` n `235`; crypto_major avg `0.105` n `8`; equity avg `-0.0069` n `151`; fx avg `0.0041` n `6`; index avg `-0.0009` n `26`; metal avg `0.0024` n `20`; unknown avg `0.1445` n `1131`
- 1h: commodity avg `0.1439` n `13`; crypto_alt avg `-0.1143` n `235`; crypto_major avg `-0.0174` n `8`; equity avg `-0.2928` n `151`; fx avg `0.0133` n `6`; index avg `-0.0292` n `26`; metal avg `-0.0115` n `20`; unknown avg `0.6278` n `1115`
- 4h: commodity avg `0.7149` n `13`; crypto_alt avg `0.6555` n `235`; crypto_major avg `0.3714` n `8`; equity avg `-0.084` n `151`; fx avg `0.061` n `6`; index avg `-0.0074` n `26`; metal avg `-0.2919` n `20`; unknown avg `1.8516` n `1091`
- 24h: commodity avg `0.2871` n `13`; crypto_alt avg `-2.0023` n `235`; crypto_major avg `-0.6027` n `8`; equity avg `-1.4557` n `151`; fx avg `0.1354` n `6`; index avg `-0.258` n `26`; metal avg `-0.1564` n `20`; unknown avg `0.8518` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1632`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1476`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1379`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0886`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
