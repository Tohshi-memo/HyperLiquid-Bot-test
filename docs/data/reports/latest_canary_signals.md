# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T20:07:33.436481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `13`; crypto_alt avg `0.1511` n `235`; crypto_major avg `0.1488` n `8`; equity avg `0.0184` n `143`; fx avg `0.0021` n `6`; index avg `-0.0024` n `26`; metal avg `-0.0007` n `20`; unknown avg `-0.0484` n `1071`
- 1h: commodity avg `-0.0026` n `13`; crypto_alt avg `0.3405` n `235`; crypto_major avg `0.128` n `8`; equity avg `0.05` n `143`; fx avg `0.0098` n `6`; index avg `0.003` n `26`; metal avg `0.0074` n `20`; unknown avg `0.2064` n `1062`
- 4h: commodity avg `-0.1005` n `13`; crypto_alt avg `0.3406` n `235`; crypto_major avg `0.4021` n `8`; equity avg `0.1042` n `143`; fx avg `-0.0055` n `6`; index avg `0.0181` n `26`; metal avg `-0.0047` n `20`; unknown avg `0.202` n `1062`
- 24h: commodity avg `0.0012` n `13`; crypto_alt avg `2.8764` n `235`; crypto_major avg `1.527` n `8`; equity avg `0.1515` n `143`; fx avg `-0.0411` n `6`; index avg `0.0304` n `26`; metal avg `-0.0275` n `20`; unknown avg `-0.363` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1995`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
