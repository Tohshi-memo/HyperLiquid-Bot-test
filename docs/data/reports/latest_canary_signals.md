# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T19:40:22.434289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `0.0296` n `230`; crypto_major avg `0.041` n `8`; equity avg `0.0084` n `114`; fx avg `-0.0022` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0388` n `791`
- 1h: commodity avg `0.0317` n `12`; crypto_alt avg `0.0315` n `230`; crypto_major avg `0.0958` n `8`; equity avg `0.0476` n `114`; fx avg `0.0` n `6`; index avg `0.0023` n `25`; metal avg `0.0003` n `20`; unknown avg `0.0311` n `791`
- 4h: commodity avg `0.089` n `12`; crypto_alt avg `-0.0623` n `230`; crypto_major avg `0.071` n `8`; equity avg `0.0734` n `114`; fx avg `-0.0019` n `6`; index avg `0.0047` n `25`; metal avg `0.0002` n `20`; unknown avg `0.0075` n `791`
- 24h: commodity avg `-0.002` n `12`; crypto_alt avg `1.0496` n `230`; crypto_major avg `0.7076` n `8`; equity avg `0.3676` n `114`; fx avg `0.021` n `6`; index avg `0.026` n `25`; metal avg `0.0174` n `20`; unknown avg `0.1557` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
