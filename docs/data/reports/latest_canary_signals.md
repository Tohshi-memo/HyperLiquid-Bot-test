# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T07:52:26.560792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0528` n `13`; crypto_alt avg `0.1378` n `239`; crypto_major avg `0.1105` n `8`; equity avg `0.1501` n `161`; fx avg `-0.0021` n `6`; index avg `0.0128` n `27`; metal avg `-0.0306` n `20`; unknown avg `0.0005` n `1259`
- 1h: commodity avg `-0.0166` n `13`; crypto_alt avg `0.2204` n `239`; crypto_major avg `0.3481` n `8`; equity avg `-0.0275` n `161`; fx avg `0.0225` n `6`; index avg `-0.0378` n `27`; metal avg `0.0029` n `20`; unknown avg `7.1743` n `1253`
- 4h: commodity avg `0.0156` n `13`; crypto_alt avg `-0.9354` n `239`; crypto_major avg `-0.2551` n `8`; equity avg `0.4397` n `161`; fx avg `-0.033` n `6`; index avg `0.017` n `27`; metal avg `0.1454` n `20`; unknown avg `0.1129` n `1211`
- 24h: commodity avg `0.4218` n `13`; crypto_alt avg `-1.3282` n `239`; crypto_major avg `-2.5294` n `8`; equity avg `1.6143` n `161`; fx avg `-0.1791` n `6`; index avg `0.1915` n `27`; metal avg `0.0317` n `20`; unknown avg `1.4148` n `1158`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
