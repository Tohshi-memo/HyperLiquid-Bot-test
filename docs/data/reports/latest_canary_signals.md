# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T08:22:30.476264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0275` n `13`; crypto_alt avg `0.1419` n `237`; crypto_major avg `0.1072` n `8`; equity avg `0.0996` n `151`; fx avg `0.0109` n `6`; index avg `0.0259` n `26`; metal avg `0.029` n `20`; unknown avg `0.1521` n `1198`
- 1h: commodity avg `0.0059` n `13`; crypto_alt avg `-0.2653` n `237`; crypto_major avg `-0.2436` n `8`; equity avg `-0.1696` n `151`; fx avg `0.0001` n `6`; index avg `-0.0147` n `26`; metal avg `-0.0811` n `20`; unknown avg `-0.0496` n `1180`
- 4h: commodity avg `0.117` n `13`; crypto_alt avg `-0.9303` n `237`; crypto_major avg `-0.8451` n `8`; equity avg `-0.5059` n `151`; fx avg `-0.0111` n `6`; index avg `-0.0461` n `26`; metal avg `-0.1146` n `20`; unknown avg `2.4216` n `1158`
- 24h: commodity avg `0.4385` n `13`; crypto_alt avg `-0.4968` n `237`; crypto_major avg `-1.0911` n `8`; equity avg `-1.5397` n `151`; fx avg `0.033` n `6`; index avg `-0.2197` n `26`; metal avg `-0.2116` n `20`; unknown avg `4.6834` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
