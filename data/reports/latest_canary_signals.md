# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T22:07:32.452763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `13`; crypto_alt avg `-0.0929` n `235`; crypto_major avg `0.0638` n `8`; equity avg `0.0134` n `143`; fx avg `0.0014` n `6`; index avg `0.0` n `26`; metal avg `-0.0049` n `20`; unknown avg `-0.0162` n `1075`
- 1h: commodity avg `0.0163` n `13`; crypto_alt avg `0.0206` n `235`; crypto_major avg `0.1237` n `8`; equity avg `0.0493` n `143`; fx avg `0.0009` n `6`; index avg `0.0076` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.0974` n `1061`
- 4h: commodity avg `0.176` n `13`; crypto_alt avg `0.1409` n `235`; crypto_major avg `-0.1325` n `8`; equity avg `0.0625` n `143`; fx avg `0.0145` n `6`; index avg `0.011` n `26`; metal avg `0.0006` n `20`; unknown avg `0.2227` n `1046`
- 24h: commodity avg `0.0409` n `13`; crypto_alt avg `2.4331` n `235`; crypto_major avg `1.3478` n `8`; equity avg `0.2254` n `143`; fx avg `-0.0141` n `6`; index avg `0.1119` n `26`; metal avg `-0.0262` n `20`; unknown avg `0.1118` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
