# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T11:17:33.839581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0393` n `12`; crypto_alt avg `-0.0291` n `229`; crypto_major avg `-0.0615` n `8`; equity avg `-0.0273` n `91`; fx avg `0.0005` n `6`; index avg `0.0085` n `25`; metal avg `0.0325` n `20`; unknown avg `-0.0146` n `763`
- 1h: commodity avg `0.0943` n `12`; crypto_alt avg `-0.2356` n `229`; crypto_major avg `-0.4031` n `8`; equity avg `-0.2635` n `91`; fx avg `-0.0313` n `6`; index avg `-0.0833` n `25`; metal avg `-0.0701` n `20`; unknown avg `-0.0819` n `763`
- 4h: commodity avg `0.0442` n `12`; crypto_alt avg `-0.1346` n `229`; crypto_major avg `-0.5279` n `8`; equity avg `-0.5209` n `91`; fx avg `-0.1218` n `6`; index avg `-0.1097` n `25`; metal avg `0.1367` n `20`; unknown avg `-0.4916` n `757`
- 24h: commodity avg `0.4563` n `12`; crypto_alt avg `0.3165` n `229`; crypto_major avg `-0.5431` n `8`; equity avg `-1.667` n `90`; fx avg `-0.1531` n `6`; index avg `-0.4274` n `25`; metal avg `-0.3137` n `20`; unknown avg `-0.4657` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
