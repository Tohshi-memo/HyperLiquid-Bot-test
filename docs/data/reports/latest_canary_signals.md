# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T17:37:30.737734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `13`; crypto_alt avg `-0.3394` n `237`; crypto_major avg `-0.243` n `8`; equity avg `-0.0961` n `151`; fx avg `0.0048` n `6`; index avg `-0.0077` n `26`; metal avg `0.0447` n `20`; unknown avg `0.0278` n `1196`
- 1h: commodity avg `0.1287` n `13`; crypto_alt avg `-0.5654` n `237`; crypto_major avg `-0.2484` n `8`; equity avg `-0.3744` n `151`; fx avg `0.0082` n `6`; index avg `-0.0564` n `26`; metal avg `0.0153` n `20`; unknown avg `-0.0556` n `1194`
- 4h: commodity avg `0.3592` n `13`; crypto_alt avg `-0.3987` n `237`; crypto_major avg `-0.6345` n `8`; equity avg `-0.6207` n `151`; fx avg `-0.0038` n `6`; index avg `-0.0552` n `26`; metal avg `-0.0768` n `20`; unknown avg `-0.2477` n `1133`
- 24h: commodity avg `-0.012` n `13`; crypto_alt avg `1.0613` n `237`; crypto_major avg `1.252` n `8`; equity avg `2.8495` n `151`; fx avg `-0.0213` n `6`; index avg `0.555` n `26`; metal avg `0.125` n `20`; unknown avg `2.7463` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
