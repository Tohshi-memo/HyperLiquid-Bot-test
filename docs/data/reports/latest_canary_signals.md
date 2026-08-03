# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T05:07:27.098738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0291` n `230`; crypto_major avg `-0.0941` n `8`; equity avg `-0.1015` n `102`; fx avg `-0.0095` n `6`; index avg `-0.0325` n `25`; metal avg `-0.0515` n `20`; unknown avg `1.3926` n `784`
- 1h: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.0609` n `230`; crypto_major avg `-0.1052` n `8`; equity avg `-0.1073` n `102`; fx avg `0.0076` n `6`; index avg `-0.0177` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.1227` n `784`
- 4h: commodity avg `-0.1814` n `12`; crypto_alt avg `-0.4455` n `230`; crypto_major avg `-0.5422` n `8`; equity avg `-0.1006` n `102`; fx avg `0.0244` n `6`; index avg `0.0134` n `25`; metal avg `0.0293` n `20`; unknown avg `0.9362` n `784`
- 24h: commodity avg `-0.3141` n `12`; crypto_alt avg `-0.9243` n `230`; crypto_major avg `-0.7149` n `8`; equity avg `0.753` n `102`; fx avg `-0.2318` n `6`; index avg `-0.0061` n `25`; metal avg `-0.0458` n `20`; unknown avg `1.2779` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
