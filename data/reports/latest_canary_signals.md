# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T17:52:34.426215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.0975` n `230`; crypto_major avg `-0.1392` n `8`; equity avg `0.026` n `113`; fx avg `0.0074` n `6`; index avg `-0.0073` n `25`; metal avg `-0.0151` n `20`; unknown avg `-0.118` n `785`
- 1h: commodity avg `0.0926` n `12`; crypto_alt avg `0.1773` n `230`; crypto_major avg `0.2927` n `8`; equity avg `0.0992` n `113`; fx avg `0.0199` n `6`; index avg `0.0008` n `25`; metal avg `0.0533` n `20`; unknown avg `-0.0356` n `785`
- 4h: commodity avg `0.2247` n `12`; crypto_alt avg `-0.3386` n `230`; crypto_major avg `-0.2261` n `8`; equity avg `-0.0366` n `113`; fx avg `0.0098` n `6`; index avg `-0.0077` n `25`; metal avg `0.3357` n `20`; unknown avg `0.5622` n `784`
- 24h: commodity avg `1.2617` n `12`; crypto_alt avg `-0.7255` n `230`; crypto_major avg `-1.3098` n `8`; equity avg `-1.2879` n `113`; fx avg `0.2536` n `6`; index avg `-0.0717` n `25`; metal avg `0.0083` n `20`; unknown avg `103.3066` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
