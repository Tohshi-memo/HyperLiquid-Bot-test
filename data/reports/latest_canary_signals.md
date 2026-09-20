# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T19:22:28.249773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `-0.0483` n `234`; crypto_major avg `0.0174` n `8`; equity avg `0.0161` n `140`; fx avg `-0.0146` n `6`; index avg `-0.0006` n `26`; metal avg `0.0098` n `20`; unknown avg `8.0564` n `943`
- 1h: commodity avg `0.0282` n `12`; crypto_alt avg `-0.3466` n `234`; crypto_major avg `-0.0826` n `8`; equity avg `0.0052` n `140`; fx avg `-0.0336` n `6`; index avg `-0.0012` n `26`; metal avg `0.0029` n `20`; unknown avg `7.45` n `933`
- 4h: commodity avg `0.0225` n `12`; crypto_alt avg `1.9921` n `234`; crypto_major avg `1.2153` n `8`; equity avg `0.223` n `140`; fx avg `-0.0057` n `6`; index avg `0.0314` n `26`; metal avg `-0.0043` n `20`; unknown avg `7.596` n `871`
- 24h: commodity avg `0.3537` n `12`; crypto_alt avg `0.0178` n `234`; crypto_major avg `-0.6651` n `8`; equity avg `-0.0869` n `140`; fx avg `-0.0576` n `6`; index avg `-0.0406` n `26`; metal avg `-0.0365` n `20`; unknown avg `6.2241` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
