# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T11:37:31.328671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `0.0803` n `239`; crypto_major avg `0.0951` n `8`; equity avg `0.0616` n `163`; fx avg `-0.0069` n `6`; index avg `-0.0006` n `27`; metal avg `0.0376` n `20`; unknown avg `1.6055` n `1266`
- 1h: commodity avg `0.0939` n `13`; crypto_alt avg `-0.1146` n `239`; crypto_major avg `-0.152` n `8`; equity avg `-0.2277` n `163`; fx avg `-0.0016` n `6`; index avg `-0.0402` n `27`; metal avg `-0.032` n `20`; unknown avg `0.3145` n `1262`
- 4h: commodity avg `0.1938` n `13`; crypto_alt avg `0.2461` n `239`; crypto_major avg `-0.2504` n `8`; equity avg `0.2099` n `163`; fx avg `-0.0021` n `6`; index avg `0.0597` n `27`; metal avg `-0.1316` n `20`; unknown avg `147.2262` n `1188`
- 24h: commodity avg `-0.1224` n `13`; crypto_alt avg `0.0786` n `239`; crypto_major avg `0.1417` n `8`; equity avg `0.3069` n `163`; fx avg `-0.0945` n `6`; index avg `0.0075` n `27`; metal avg `-1.1067` n `20`; unknown avg `6.1849` n `1099`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
