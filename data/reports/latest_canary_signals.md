# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T04:52:29.876768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0132` n `12`; crypto_alt avg `0.1756` n `230`; crypto_major avg `0.1351` n `8`; equity avg `0.0293` n `102`; fx avg `0.0026` n `6`; index avg `0.0106` n `25`; metal avg `-0.0293` n `20`; unknown avg `2.0524` n `774`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.0369` n `230`; crypto_major avg `-0.0053` n `8`; equity avg `-0.2389` n `102`; fx avg `-0.0025` n `6`; index avg `-0.0594` n `25`; metal avg `-0.0484` n `20`; unknown avg `1.9663` n `774`
- 4h: commodity avg `-0.1427` n `12`; crypto_alt avg `-0.1133` n `230`; crypto_major avg `-0.1425` n `8`; equity avg `-0.8084` n `102`; fx avg `-0.04` n `6`; index avg `-0.1193` n `25`; metal avg `-0.153` n `20`; unknown avg `0.2531` n `774`
- 24h: commodity avg `-0.753` n `12`; crypto_alt avg `-3.8081` n `230`; crypto_major avg `-3.3592` n `8`; equity avg `-3.5002` n `102`; fx avg `-0.1181` n `6`; index avg `-0.7608` n `25`; metal avg `-0.2871` n `20`; unknown avg `1161.8373` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
