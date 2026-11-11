# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T14:07:27.070798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.022` n `13`; crypto_alt avg `0.099` n `239`; crypto_major avg `0.1355` n `8`; equity avg `-0.0363` n `161`; fx avg `-0.0291` n `6`; index avg `-0.0078` n `27`; metal avg `-0.0425` n `20`; unknown avg `19.6967` n `1257`
- 1h: commodity avg `-0.0385` n `13`; crypto_alt avg `0.3768` n `239`; crypto_major avg `0.3803` n `8`; equity avg `0.0187` n `161`; fx avg `-0.0176` n `6`; index avg `-0.0083` n `27`; metal avg `-0.0444` n `20`; unknown avg `19.6476` n `1255`
- 4h: commodity avg `0.0806` n `13`; crypto_alt avg `0.7314` n `239`; crypto_major avg `0.564` n `8`; equity avg `0.3034` n `161`; fx avg `-0.0215` n `6`; index avg `0.022` n `27`; metal avg `-0.1752` n `20`; unknown avg `1.6788` n `1247`
- 24h: commodity avg `1.0772` n `13`; crypto_alt avg `-0.1263` n `239`; crypto_major avg `-0.3643` n `8`; equity avg `4.2232` n `161`; fx avg `-0.2394` n `6`; index avg `0.3679` n `27`; metal avg `0.2922` n `20`; unknown avg `2.7829` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2872`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
