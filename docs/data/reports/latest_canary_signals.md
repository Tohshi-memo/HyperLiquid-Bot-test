# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T09:52:26.696926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `12`; crypto_alt avg `0.024` n `230`; crypto_major avg `0.0106` n `8`; equity avg `0.0288` n `114`; fx avg `0.001` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.0053` n `791`
- 1h: commodity avg `0.0341` n `12`; crypto_alt avg `0.0129` n `230`; crypto_major avg `0.0421` n `8`; equity avg `0.0103` n `114`; fx avg `0.0013` n `6`; index avg `-0.0111` n `25`; metal avg `0.0064` n `20`; unknown avg `0.0059` n `791`
- 4h: commodity avg `-0.1826` n `12`; crypto_alt avg `0.0279` n `230`; crypto_major avg `-0.0995` n `8`; equity avg `0.0528` n `114`; fx avg `-0.0025` n `6`; index avg `-0.0` n `25`; metal avg `0.01` n `20`; unknown avg `-0.0424` n `765`
- 24h: commodity avg `-0.1136` n `12`; crypto_alt avg `1.179` n `230`; crypto_major avg `0.0778` n `8`; equity avg `-0.4202` n `114`; fx avg `0.1715` n `6`; index avg `-0.1276` n `25`; metal avg `0.1773` n `20`; unknown avg `-0.0695` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
