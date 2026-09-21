# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T23:52:27.132706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `0.0612` n `234`; crypto_major avg `0.0019` n `8`; equity avg `0.0361` n `140`; fx avg `0.0047` n `6`; index avg `-0.0053` n `26`; metal avg `0.0227` n `20`; unknown avg `0.1511` n `944`
- 1h: commodity avg `0.0479` n `12`; crypto_alt avg `0.2451` n `234`; crypto_major avg `-0.145` n `8`; equity avg `0.2063` n `140`; fx avg `-0.0048` n `6`; index avg `0.0022` n `26`; metal avg `0.0567` n `20`; unknown avg `0.5476` n `942`
- 4h: commodity avg `0.0509` n `12`; crypto_alt avg `0.5468` n `234`; crypto_major avg `0.6305` n `8`; equity avg `0.3737` n `140`; fx avg `-0.0244` n `6`; index avg `0.0091` n `26`; metal avg `0.1286` n `20`; unknown avg `0.0551` n `852`
- 24h: commodity avg `-0.6589` n `12`; crypto_alt avg `3.9387` n `234`; crypto_major avg `5.4237` n `8`; equity avg `2.7079` n `140`; fx avg `-0.1348` n `6`; index avg `0.5513` n `26`; metal avg `0.1389` n `20`; unknown avg `8.3056` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
