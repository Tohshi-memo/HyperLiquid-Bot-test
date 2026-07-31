# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T10:11:59.961662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0396` n `12`; crypto_alt avg `-0.091` n `230`; crypto_major avg `-0.0712` n `8`; equity avg `0.004` n `102`; fx avg `0.016` n `6`; index avg `-0.0201` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0694` n `780`
- 1h: commodity avg `0.2344` n `12`; crypto_alt avg `-0.2611` n `230`; crypto_major avg `-0.3714` n `8`; equity avg `-0.3694` n `102`; fx avg `0.1424` n `6`; index avg `-0.0646` n `25`; metal avg `-0.0484` n `20`; unknown avg `-0.0033` n `780`
- 4h: commodity avg `0.4219` n `12`; crypto_alt avg `-0.4754` n `230`; crypto_major avg `-0.8905` n `8`; equity avg `-0.4211` n `102`; fx avg `-0.0118` n `6`; index avg `-0.1188` n `25`; metal avg `-0.1963` n `20`; unknown avg `0.1063` n `779`
- 24h: commodity avg `0.0413` n `12`; crypto_alt avg `-0.6378` n `230`; crypto_major avg `-0.5481` n `8`; equity avg `8.0961` n `102`; fx avg `-0.1619` n `6`; index avg `1.1551` n `25`; metal avg `0.0856` n `20`; unknown avg `-0.0378` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
