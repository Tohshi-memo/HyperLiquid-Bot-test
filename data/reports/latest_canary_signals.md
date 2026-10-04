# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T05:45:24.809679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `13`; crypto_alt avg `-0.0368` n `235`; crypto_major avg `0.0682` n `8`; equity avg `0.0097` n `143`; fx avg `-0.0005` n `6`; index avg `0.0009` n `26`; metal avg `0.0029` n `20`; unknown avg `-0.2194` n `1079`
- 1h: commodity avg `0.0181` n `13`; crypto_alt avg `0.1711` n `235`; crypto_major avg `0.1608` n `8`; equity avg `0.0162` n `143`; fx avg `-0.02` n `6`; index avg `0.0032` n `26`; metal avg `0.0012` n `20`; unknown avg `-0.1044` n `1077`
- 4h: commodity avg `-0.0423` n `13`; crypto_alt avg `0.697` n `235`; crypto_major avg `0.2598` n `8`; equity avg `0.077` n `143`; fx avg `-0.0183` n `6`; index avg `0.0028` n `26`; metal avg `0.0113` n `20`; unknown avg `-0.1756` n `1071`
- 24h: commodity avg `0.1994` n `13`; crypto_alt avg `1.8251` n `235`; crypto_major avg `0.9015` n `8`; equity avg `0.2789` n `143`; fx avg `-0.03` n `6`; index avg `0.0103` n `26`; metal avg `0.009` n `20`; unknown avg `0.3061` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
