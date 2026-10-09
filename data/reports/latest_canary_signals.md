# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T02:07:29.967690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `13`; crypto_alt avg `0.1019` n `235`; crypto_major avg `0.1234` n `8`; equity avg `-0.0668` n `150`; fx avg `0.0191` n `6`; index avg `-0.0038` n `26`; metal avg `-0.009` n `20`; unknown avg `1.1633` n `1076`
- 1h: commodity avg `-0.1395` n `13`; crypto_alt avg `0.9831` n `235`; crypto_major avg `0.5049` n `8`; equity avg `0.4251` n `150`; fx avg `-0.0073` n `6`; index avg `0.0567` n `26`; metal avg `0.1718` n `20`; unknown avg `1.2283` n `1076`
- 4h: commodity avg `-0.1618` n `13`; crypto_alt avg `0.7829` n `235`; crypto_major avg `0.322` n `8`; equity avg `0.4111` n `150`; fx avg `0.047` n `6`; index avg `0.0802` n `26`; metal avg `0.4035` n `20`; unknown avg `0.7301` n `1069`
- 24h: commodity avg `0.2462` n `13`; crypto_alt avg `-2.5134` n `235`; crypto_major avg `-3.1469` n `8`; equity avg `-2.3475` n `150`; fx avg `0.133` n `6`; index avg `-0.2739` n `26`; metal avg `0.0295` n `20`; unknown avg `5.8527` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
