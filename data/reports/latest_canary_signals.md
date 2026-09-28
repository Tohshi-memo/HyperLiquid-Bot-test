# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T01:22:31.909523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0951` n `12`; crypto_alt avg `-0.4103` n `234`; crypto_major avg `-0.1652` n `8`; equity avg `-0.1752` n `141`; fx avg `0.025` n `6`; index avg `-0.0287` n `26`; metal avg `-0.0684` n `20`; unknown avg `3.4668` n `962`
- 1h: commodity avg `0.0096` n `12`; crypto_alt avg `-0.9117` n `234`; crypto_major avg `-0.83` n `8`; equity avg `-0.7603` n `141`; fx avg `0.0249` n `6`; index avg `-0.1263` n `26`; metal avg `-0.3084` n `20`; unknown avg `28.5562` n `960`
- 4h: commodity avg `-0.3488` n `12`; crypto_alt avg `-0.3582` n `234`; crypto_major avg `-0.6022` n `8`; equity avg `-0.9666` n `141`; fx avg `0.1275` n `6`; index avg `-0.1274` n `26`; metal avg `-0.5394` n `20`; unknown avg `3.886` n `920`
- 24h: commodity avg `-0.3942` n `12`; crypto_alt avg `0.7729` n `234`; crypto_major avg `-0.2436` n `8`; equity avg `-0.6449` n `141`; fx avg `0.0701` n `6`; index avg `-0.0821` n `26`; metal avg `-0.5539` n `20`; unknown avg `12.1457` n `829`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
