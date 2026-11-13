# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T21:37:30.044999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0463` n `13`; crypto_alt avg `-0.0475` n `239`; crypto_major avg `0.0429` n `8`; equity avg `-0.1246` n `162`; fx avg `-0.0104` n `6`; index avg `-0.0106` n `27`; metal avg `-0.0975` n `20`; unknown avg `0.4288` n `1262`
- 1h: commodity avg `0.1237` n `13`; crypto_alt avg `-0.5775` n `239`; crypto_major avg `-0.8361` n `8`; equity avg `-0.5785` n `162`; fx avg `-0.0106` n `6`; index avg `-0.0612` n `27`; metal avg `-0.0663` n `20`; unknown avg `2.3753` n `1226`
- 4h: commodity avg `0.1733` n `13`; crypto_alt avg `-0.6525` n `239`; crypto_major avg `-0.7171` n `8`; equity avg `-0.2164` n `162`; fx avg `-0.0409` n `6`; index avg `-0.0049` n `27`; metal avg `-0.2006` n `20`; unknown avg `2.6706` n `1216`
- 24h: commodity avg `-0.2212` n `13`; crypto_alt avg `-1.2775` n `239`; crypto_major avg `-2.5976` n `8`; equity avg `-3.2149` n `162`; fx avg `-0.0861` n `6`; index avg `-0.2658` n `27`; metal avg `-0.3335` n `20`; unknown avg `2.664` n `1069`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
