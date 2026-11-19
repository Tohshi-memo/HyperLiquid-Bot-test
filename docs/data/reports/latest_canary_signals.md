# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T11:37:33.211799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1184` n `13`; crypto_alt avg `0.2575` n `239`; crypto_major avg `0.3416` n `8`; equity avg `0.3085` n `164`; fx avg `-0.0141` n `6`; index avg `0.033` n `27`; metal avg `0.0201` n `20`; unknown avg `0.1891` n `1266`
- 1h: commodity avg `-0.2453` n `13`; crypto_alt avg `0.3461` n `239`; crypto_major avg `0.4352` n `8`; equity avg `0.3557` n `164`; fx avg `-0.0295` n `6`; index avg `0.029` n `27`; metal avg `-0.0168` n `20`; unknown avg `-0.0205` n `1264`
- 4h: commodity avg `-0.1513` n `13`; crypto_alt avg `0.4993` n `239`; crypto_major avg `0.4809` n `8`; equity avg `0.8203` n `164`; fx avg `0.0412` n `6`; index avg `0.1348` n `27`; metal avg `-0.0274` n `20`; unknown avg `353.4099` n `1224`
- 24h: commodity avg `-0.0611` n `13`; crypto_alt avg `0.4546` n `239`; crypto_major avg `0.2359` n `8`; equity avg `0.9837` n `164`; fx avg `0.0408` n `6`; index avg `0.2888` n `27`; metal avg `-0.1878` n `20`; unknown avg `1.8914` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
