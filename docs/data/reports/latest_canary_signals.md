# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T06:37:27.425704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.0188` n `230`; crypto_major avg `0.0643` n `8`; equity avg `0.0443` n `102`; fx avg `-0.0096` n `6`; index avg `-0.0074` n `25`; metal avg `0.005` n `20`; unknown avg `-0.0106` n `782`
- 1h: commodity avg `-0.0647` n `12`; crypto_alt avg `0.0262` n `230`; crypto_major avg `-0.0384` n `8`; equity avg `0.1063` n `102`; fx avg `-0.0073` n `6`; index avg `0.0182` n `25`; metal avg `-0.0073` n `20`; unknown avg `0.0239` n `766`
- 4h: commodity avg `-0.2442` n `12`; crypto_alt avg `0.3013` n `230`; crypto_major avg `0.3323` n `8`; equity avg `0.1417` n `102`; fx avg `-0.0745` n `6`; index avg `0.0817` n `25`; metal avg `0.0969` n `20`; unknown avg `0.3889` n `766`
- 24h: commodity avg `-1.0842` n `12`; crypto_alt avg `0.2304` n `230`; crypto_major avg `0.4446` n `8`; equity avg `0.8466` n `102`; fx avg `-0.1347` n `6`; index avg `0.2484` n `25`; metal avg `0.2672` n `20`; unknown avg `0.3528` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
