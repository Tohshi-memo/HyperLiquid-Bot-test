# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T09:52:30.015695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.1431` n `234`; crypto_major avg `-0.0692` n `8`; equity avg `-0.0038` n `140`; fx avg `-0.0012` n `6`; index avg `0.0106` n `26`; metal avg `-0.0008` n `20`; unknown avg `-0.135` n `943`
- 1h: commodity avg `-0.046` n `12`; crypto_alt avg `0.3571` n `234`; crypto_major avg `0.3912` n `8`; equity avg `0.0428` n `140`; fx avg `-0.0023` n `6`; index avg `0.0091` n `26`; metal avg `0.027` n `20`; unknown avg `0.2712` n `941`
- 4h: commodity avg `0.0001` n `12`; crypto_alt avg `-0.5762` n `234`; crypto_major avg `0.017` n `8`; equity avg `-0.0377` n `140`; fx avg `0.0084` n `6`; index avg `-0.0034` n `26`; metal avg `0.0244` n `20`; unknown avg `0.5787` n `905`
- 24h: commodity avg `0.2422` n `12`; crypto_alt avg `-1.3415` n `234`; crypto_major avg `-1.7514` n `8`; equity avg `-0.2482` n `140`; fx avg `-0.0714` n `6`; index avg `-0.0557` n `26`; metal avg `0.0362` n `20`; unknown avg `0.7086` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
