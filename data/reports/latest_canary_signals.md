# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T05:22:23.481764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `13`; crypto_alt avg `-0.17` n `235`; crypto_major avg `-0.0861` n `8`; equity avg `-0.0823` n `151`; fx avg `0.0116` n `6`; index avg `-0.0277` n `26`; metal avg `-0.0373` n `20`; unknown avg `-0.2056` n `1135`
- 1h: commodity avg `-0.0032` n `13`; crypto_alt avg `-0.1595` n `235`; crypto_major avg `-0.1538` n `8`; equity avg `-0.337` n `151`; fx avg `-0.0085` n `6`; index avg `-0.0587` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.3081` n `1133`
- 4h: commodity avg `-0.1779` n `13`; crypto_alt avg `-0.0244` n `235`; crypto_major avg `0.0293` n `8`; equity avg `-0.1616` n `151`; fx avg `-0.0393` n `6`; index avg `0.025` n `26`; metal avg `0.1393` n `20`; unknown avg `-0.465` n `1127`
- 24h: commodity avg `1.0541` n `13`; crypto_alt avg `-0.963` n `235`; crypto_major avg `-0.4436` n `8`; equity avg `-0.0935` n `151`; fx avg `0.0147` n `6`; index avg `0.0549` n `26`; metal avg `-0.3559` n `20`; unknown avg `0.7535` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1542`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1368`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0831`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `666`, weak_sample_signal
