# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T19:07:25.674336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1027` n `13`; crypto_alt avg `-0.2233` n `235`; crypto_major avg `-0.1655` n `8`; equity avg `-0.1486` n `150`; fx avg `0.008` n `6`; index avg `-0.0268` n `26`; metal avg `-0.0806` n `20`; unknown avg `0.649` n `1075`
- 1h: commodity avg `0.3505` n `13`; crypto_alt avg `-0.1089` n `235`; crypto_major avg `-0.0024` n `8`; equity avg `-0.1351` n `150`; fx avg `0.0103` n `6`; index avg `-0.0255` n `26`; metal avg `-0.1211` n `20`; unknown avg `1.9662` n `1075`
- 4h: commodity avg `-0.3133` n `13`; crypto_alt avg `0.7213` n `235`; crypto_major avg `0.0873` n `8`; equity avg `0.2116` n `150`; fx avg `-0.0037` n `6`; index avg `0.1054` n `26`; metal avg `-0.0301` n `20`; unknown avg `1.9241` n `1068`
- 24h: commodity avg `0.3993` n `13`; crypto_alt avg `-4.7804` n `235`; crypto_major avg `-3.4684` n `8`; equity avg `-1.5567` n `150`; fx avg `-0.1663` n `6`; index avg `-0.2522` n `26`; metal avg `-0.8167` n `20`; unknown avg `15.4374` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
