# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T00:37:22.885815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0237` n `12`; crypto_alt avg `-0.0294` n `230`; crypto_major avg `-0.031` n `8`; equity avg `-0.0874` n `102`; fx avg `-0.1393` n `6`; index avg `-0.0436` n `25`; metal avg `-0.0383` n `20`; unknown avg `-0.0221` n `784`
- 1h: commodity avg `-0.0216` n `12`; crypto_alt avg `-0.1858` n `230`; crypto_major avg `-0.298` n `8`; equity avg `-0.0426` n `102`; fx avg `-0.2093` n `6`; index avg `-0.1466` n `25`; metal avg `-0.1071` n `20`; unknown avg `-0.0221` n `784`
- 4h: commodity avg `-0.1177` n `12`; crypto_alt avg `-0.2222` n `230`; crypto_major avg `-0.1343` n `8`; equity avg `0.1263` n `102`; fx avg `-0.1473` n `6`; index avg `-0.1186` n `25`; metal avg `-0.2294` n `20`; unknown avg `1.9988` n `783`
- 24h: commodity avg `-1.0792` n `12`; crypto_alt avg `0.8292` n `230`; crypto_major avg `1.337` n `8`; equity avg `1.314` n `102`; fx avg `-0.1903` n `6`; index avg `0.1344` n `25`; metal avg `0.1014` n `20`; unknown avg `1.5423` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
