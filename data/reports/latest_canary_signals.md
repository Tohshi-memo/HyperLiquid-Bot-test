# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T07:52:34.711066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `13`; crypto_alt avg `0.1294` n `235`; crypto_major avg `0.089` n `8`; equity avg `-0.0023` n `143`; fx avg `0.0` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0006` n `20`; unknown avg `2.4406` n `1079`
- 1h: commodity avg `-0.0209` n `13`; crypto_alt avg `0.1358` n `235`; crypto_major avg `0.029` n `8`; equity avg `-0.0188` n `143`; fx avg `0.0025` n `6`; index avg `-0.0077` n `26`; metal avg `0.0005` n `20`; unknown avg `2.0819` n `1077`
- 4h: commodity avg `0.0037` n `13`; crypto_alt avg `0.6854` n `235`; crypto_major avg `0.2483` n `8`; equity avg `-0.0122` n `143`; fx avg `-0.0214` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0055` n `20`; unknown avg `1.7747` n `1043`
- 24h: commodity avg `0.1546` n `13`; crypto_alt avg `2.5355` n `235`; crypto_major avg `1.0899` n `8`; equity avg `0.2443` n `143`; fx avg `-0.0396` n `6`; index avg `0.0145` n `26`; metal avg `0.0062` n `20`; unknown avg `0.4073` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
