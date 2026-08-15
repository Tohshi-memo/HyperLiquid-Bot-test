# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T11:37:25.121056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0426` n `12`; crypto_alt avg `-0.0021` n `230`; crypto_major avg `-0.0208` n `8`; equity avg `-0.0154` n `114`; fx avg `-0.0011` n `6`; index avg `0.001` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.0584` n `791`
- 1h: commodity avg `0.0955` n `12`; crypto_alt avg `-0.0872` n `230`; crypto_major avg `-0.0024` n `8`; equity avg `0.0034` n `114`; fx avg `-0.0006` n `6`; index avg `0.0015` n `25`; metal avg `0.012` n `20`; unknown avg `0.0626` n `791`
- 4h: commodity avg `0.1034` n `12`; crypto_alt avg `0.0444` n `230`; crypto_major avg `-0.1322` n `8`; equity avg `-0.0103` n `114`; fx avg `-0.0063` n `6`; index avg `-0.0131` n `25`; metal avg `0.0162` n `20`; unknown avg `-0.0122` n `791`
- 24h: commodity avg `0.0796` n `12`; crypto_alt avg `0.9924` n `230`; crypto_major avg `0.0657` n `8`; equity avg `-0.6835` n `114`; fx avg `0.1154` n `6`; index avg `-0.1563` n `25`; metal avg `0.1307` n `20`; unknown avg `-0.041` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
