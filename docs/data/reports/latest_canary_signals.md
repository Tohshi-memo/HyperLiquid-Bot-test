# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T16:52:34.550700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `12`; crypto_alt avg `0.6194` n `234`; crypto_major avg `0.6404` n `8`; equity avg `0.1834` n `140`; fx avg `-0.0247` n `6`; index avg `0.0371` n `26`; metal avg `0.0828` n `20`; unknown avg `24.0942` n `910`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `0.2998` n `234`; crypto_major avg `0.0907` n `8`; equity avg `0.1825` n `140`; fx avg `-0.0186` n `6`; index avg `0.0544` n `26`; metal avg `0.1135` n `20`; unknown avg `23.2709` n `888`
- 4h: commodity avg `0.4513` n `12`; crypto_alt avg `0.6605` n `234`; crypto_major avg `0.4614` n `8`; equity avg `0.8719` n `140`; fx avg `-0.0647` n `6`; index avg `0.1242` n `26`; metal avg `0.0129` n `20`; unknown avg `24.5747` n `858`
- 24h: commodity avg `0.3929` n `12`; crypto_alt avg `1.449` n `234`; crypto_major avg `1.2686` n `8`; equity avg `0.7706` n `140`; fx avg `-0.29` n `6`; index avg `0.1192` n `26`; metal avg `0.0707` n `20`; unknown avg `0.8434` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
