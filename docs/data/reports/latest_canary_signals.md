# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T20:07:30.125232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `0.217` n `234`; crypto_major avg `-0.005` n `8`; equity avg `0.0164` n `141`; fx avg `-0.0021` n `6`; index avg `-0.0003` n `26`; metal avg `0.0027` n `20`; unknown avg `6.8921` n `954`
- 1h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.125` n `234`; crypto_major avg `-0.0508` n `8`; equity avg `0.0457` n `141`; fx avg `-0.0021` n `6`; index avg `0.0065` n `26`; metal avg `0.0043` n `20`; unknown avg `3.6151` n `928`
- 4h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.9912` n `234`; crypto_major avg `0.2895` n `8`; equity avg `0.1348` n `141`; fx avg `-0.0033` n `6`; index avg `0.0123` n `26`; metal avg `0.0127` n `20`; unknown avg `3.7958` n `928`
- 24h: commodity avg `-0.1432` n `12`; crypto_alt avg `1.097` n `234`; crypto_major avg `0.6327` n `8`; equity avg `0.4055` n `141`; fx avg `-0.019` n `6`; index avg `0.0398` n `26`; metal avg `-0.0058` n `20`; unknown avg `8.1685` n `871`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
