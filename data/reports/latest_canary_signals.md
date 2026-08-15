# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T22:22:28.882578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.0012` n `230`; crypto_major avg `-0.016` n `8`; equity avg `-0.0088` n `114`; fx avg `-0.0025` n `6`; index avg `-0.001` n `25`; metal avg `0.0019` n `20`; unknown avg `0.0532` n `791`
- 1h: commodity avg `-0.0278` n `12`; crypto_alt avg `-0.0435` n `230`; crypto_major avg `-0.0272` n `8`; equity avg `-0.0076` n `114`; fx avg `-0.002` n `6`; index avg `0.0002` n `25`; metal avg `0.0044` n `20`; unknown avg `0.2354` n `791`
- 4h: commodity avg `-0.0183` n `12`; crypto_alt avg `0.0518` n `230`; crypto_major avg `0.1304` n `8`; equity avg `0.0422` n `114`; fx avg `0.0028` n `6`; index avg `-0.0145` n `25`; metal avg `-0.0043` n `20`; unknown avg `1.0003` n `791`
- 24h: commodity avg `-0.1167` n `12`; crypto_alt avg `0.9019` n `230`; crypto_major avg `0.5925` n `8`; equity avg `0.1219` n `114`; fx avg `0.0156` n `6`; index avg `-0.0109` n `25`; metal avg `0.0137` n `20`; unknown avg `0.1865` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
