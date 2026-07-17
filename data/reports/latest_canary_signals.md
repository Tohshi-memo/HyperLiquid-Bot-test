# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T13:37:25.188909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0181` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.07` n `12`; crypto_alt avg `-0.3306` n `230`; crypto_major avg `-0.5008` n `8`; equity avg `-0.6085` n `96`; fx avg `0.0054` n `6`; index avg `-0.0809` n `25`; metal avg `0.0166` n `20`; unknown avg `0.0732` n `769`
- 1h: commodity avg `0.1253` n `12`; crypto_alt avg `-0.9708` n `230`; crypto_major avg `-1.0027` n `8`; equity avg `-1.0435` n `96`; fx avg `0.023` n `6`; index avg `-0.1687` n `25`; metal avg `-0.0577` n `20`; unknown avg `0.187` n `769`
- 4h: commodity avg `0.269` n `12`; crypto_alt avg `-1.0618` n `230`; crypto_major avg `-1.1471` n `8`; equity avg `-0.9093` n `96`; fx avg `-0.0267` n `6`; index avg `-0.129` n `25`; metal avg `-0.2605` n `20`; unknown avg `0.2453` n `769`
- 24h: commodity avg `0.0754` n `12`; crypto_alt avg `-3.0271` n `230`; crypto_major avg `-3.9903` n `8`; equity avg `-5.3136` n `94`; fx avg `-0.0461` n `6`; index avg `-0.7672` n `25`; metal avg `-0.6653` n `20`; unknown avg `-0.4296` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
