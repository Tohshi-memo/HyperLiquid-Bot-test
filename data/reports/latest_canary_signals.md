# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T01:07:27.688925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.7624` n `234`; crypto_major avg `-0.6914` n `8`; equity avg `-0.1343` n `140`; fx avg `0.0156` n `6`; index avg `-0.0054` n `26`; metal avg `0.0162` n `20`; unknown avg `-0.1484` n `942`
- 1h: commodity avg `0.1259` n `12`; crypto_alt avg `-0.1013` n `234`; crypto_major avg `-0.5148` n `8`; equity avg `-0.0337` n `140`; fx avg `-0.0952` n `6`; index avg `0.0011` n `26`; metal avg `-0.0756` n `20`; unknown avg `0.6332` n `942`
- 4h: commodity avg `0.1613` n `12`; crypto_alt avg `0.4957` n `234`; crypto_major avg `-0.4274` n `8`; equity avg `0.4831` n `140`; fx avg `-0.1565` n `6`; index avg `0.0549` n `26`; metal avg `0.1214` n `20`; unknown avg `0.8406` n `936`
- 24h: commodity avg `-0.203` n `12`; crypto_alt avg `3.2034` n `234`; crypto_major avg `3.8907` n `8`; equity avg `2.2999` n `140`; fx avg `-0.2598` n `6`; index avg `0.5189` n `26`; metal avg `-0.0079` n `20`; unknown avg `13.0407` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
