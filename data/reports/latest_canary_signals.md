# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T13:07:26.805855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2143` n `12`; crypto_alt avg `0.4062` n `228`; crypto_major avg `0.2251` n `8`; equity avg `0.0663` n `74`; fx avg `-0.0145` n `6`; index avg `0.0751` n `23`; metal avg `0.1257` n `18`; unknown avg `0.0916` n `547`
- 1h: commodity avg `-0.1071` n `12`; crypto_alt avg `0.131` n `228`; crypto_major avg `-0.1319` n `8`; equity avg `0.0032` n `74`; fx avg `0.0047` n `6`; index avg `0.0548` n `23`; metal avg `0.0075` n `18`; unknown avg `0.0033` n `547`
- 4h: commodity avg `0.1259` n `12`; crypto_alt avg `0.6459` n `228`; crypto_major avg `-0.1531` n `8`; equity avg `0.1926` n `74`; fx avg `0.1491` n `6`; index avg `0.1244` n `23`; metal avg `0.552` n `18`; unknown avg `0.1467` n `547`
- 24h: commodity avg `-0.4024` n `12`; crypto_alt avg `-1.0484` n `228`; crypto_major avg `-0.8804` n `8`; equity avg `0.8644` n `74`; fx avg `0.1469` n `6`; index avg `0.4312` n `23`; metal avg `0.7311` n `18`; unknown avg `-0.8559` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
