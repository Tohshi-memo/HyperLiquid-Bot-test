# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T00:37:24.885378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `0.1688` n `237`; crypto_major avg `0.2092` n `8`; equity avg `0.2805` n `151`; fx avg `0.0033` n `6`; index avg `0.0525` n `26`; metal avg `0.0487` n `20`; unknown avg `0.4744` n `1198`
- 1h: commodity avg `0.0285` n `13`; crypto_alt avg `-0.4825` n `237`; crypto_major avg `-0.4787` n `8`; equity avg `-0.6694` n `151`; fx avg `-0.0332` n `6`; index avg `-0.1256` n `26`; metal avg `-0.0192` n `20`; unknown avg `0.1102` n `1190`
- 4h: commodity avg `-0.0148` n `13`; crypto_alt avg `0.3109` n `237`; crypto_major avg `0.0265` n `8`; equity avg `-0.5202` n `151`; fx avg `-0.0283` n `6`; index avg `-0.0964` n `26`; metal avg `-0.0553` n `20`; unknown avg `3.5405` n `1168`
- 24h: commodity avg `0.1605` n `13`; crypto_alt avg `0.3364` n `237`; crypto_major avg `-0.0238` n `8`; equity avg `0.2754` n `151`; fx avg `-0.0751` n `6`; index avg `0.0934` n `26`; metal avg `-0.2071` n `20`; unknown avg `5.2458` n `990`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
