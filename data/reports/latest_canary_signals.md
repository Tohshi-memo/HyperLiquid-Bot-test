# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T04:23:03.027781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `13`; crypto_alt avg `0.1214` n `235`; crypto_major avg `0.0094` n `8`; equity avg `0.0123` n `149`; fx avg `-0.0026` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0132` n `20`; unknown avg `0.0177` n `1074`
- 1h: commodity avg `-0.0479` n `13`; crypto_alt avg `0.0925` n `235`; crypto_major avg `0.0816` n `8`; equity avg `0.0284` n `149`; fx avg `0.0166` n `6`; index avg `0.0153` n `26`; metal avg `-0.0234` n `20`; unknown avg `0.1558` n `1066`
- 4h: commodity avg `0.044` n `13`; crypto_alt avg `-1.2579` n `235`; crypto_major avg `-0.5653` n `8`; equity avg `-0.1368` n `149`; fx avg `0.0359` n `6`; index avg `-0.0391` n `26`; metal avg `-0.1093` n `20`; unknown avg `0.4897` n `1066`
- 24h: commodity avg `0.0197` n `13`; crypto_alt avg `-0.5886` n `235`; crypto_major avg `0.1499` n `8`; equity avg `0.159` n `149`; fx avg `0.0617` n `6`; index avg `0.1181` n `26`; metal avg `0.0494` n `20`; unknown avg `584.5714` n `856`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
