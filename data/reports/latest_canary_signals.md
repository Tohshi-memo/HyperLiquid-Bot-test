# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T16:22:25.607359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `13`; crypto_alt avg `0.1226` n `235`; crypto_major avg `-0.0479` n `8`; equity avg `-0.0064` n `150`; fx avg `0.0011` n `6`; index avg `0.0014` n `26`; metal avg `0.0069` n `20`; unknown avg `0.5186` n `1134`
- 1h: commodity avg `0.026` n `13`; crypto_alt avg `1.1791` n `235`; crypto_major avg `0.9888` n `8`; equity avg `0.1514` n `150`; fx avg `-0.0055` n `6`; index avg `0.0165` n `26`; metal avg `0.0171` n `20`; unknown avg `2.872` n `1110`
- 4h: commodity avg `-0.0677` n `13`; crypto_alt avg `2.1593` n `235`; crypto_major avg `1.2034` n `8`; equity avg `0.1487` n `150`; fx avg `-0.0095` n `6`; index avg `0.0215` n `26`; metal avg `0.0214` n `20`; unknown avg `2.2188` n `1037`
- 24h: commodity avg `0.3288` n `13`; crypto_alt avg `2.2724` n `235`; crypto_major avg `0.8723` n `8`; equity avg `0.212` n `150`; fx avg `0.0112` n `6`; index avg `0.0058` n `26`; metal avg `0.044` n `20`; unknown avg `1.3381` n `925`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
