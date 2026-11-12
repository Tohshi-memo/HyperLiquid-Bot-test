# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T02:29:24.030484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0554` n `13`; crypto_alt avg `0.2419` n `239`; crypto_major avg `0.2873` n `8`; equity avg `0.1734` n `161`; fx avg `-0.021` n `6`; index avg `0.0215` n `27`; metal avg `0.0155` n `20`; unknown avg `0.3439` n `1258`
- 1h: commodity avg `0.0983` n `13`; crypto_alt avg `0.5172` n `239`; crypto_major avg `0.503` n `8`; equity avg `0.8554` n `161`; fx avg `-0.0423` n `6`; index avg `0.0926` n `27`; metal avg `0.0091` n `20`; unknown avg `1.0908` n `1254`
- 4h: commodity avg `0.0159` n `13`; crypto_alt avg `-1.0074` n `239`; crypto_major avg `-0.8322` n `8`; equity avg `-0.3541` n `161`; fx avg `-0.0649` n `6`; index avg `-0.0233` n `27`; metal avg `0.0234` n `20`; unknown avg `19.712` n `1248`
- 24h: commodity avg `0.2017` n `13`; crypto_alt avg `-0.7459` n `239`; crypto_major avg `0.477` n `8`; equity avg `2.1835` n `161`; fx avg `-0.1704` n `6`; index avg `0.1999` n `27`; metal avg `-0.2363` n `20`; unknown avg `3.7905` n `1141`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
