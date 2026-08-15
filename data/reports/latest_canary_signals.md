# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T01:07:27.395731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0303` n `12`; crypto_alt avg `-0.1331` n `230`; crypto_major avg `-0.0513` n `8`; equity avg `-0.0152` n `114`; fx avg `-0.0063` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0047` n `20`; unknown avg `0.1254` n `791`
- 1h: commodity avg `-0.0445` n `12`; crypto_alt avg `-0.0903` n `230`; crypto_major avg `-0.0617` n `8`; equity avg `0.0214` n `114`; fx avg `-0.0006` n `6`; index avg `-0.0005` n `25`; metal avg `0.0206` n `20`; unknown avg `0.1521` n `791`
- 4h: commodity avg `0.0671` n `12`; crypto_alt avg `0.1984` n `230`; crypto_major avg `0.2445` n `8`; equity avg `0.0022` n `114`; fx avg `-0.0275` n `6`; index avg `0.0006` n `25`; metal avg `0.0819` n `20`; unknown avg `2.352` n `791`
- 24h: commodity avg `0.1517` n `12`; crypto_alt avg `0.008` n `230`; crypto_major avg `-0.8134` n `8`; equity avg `-0.2648` n `114`; fx avg `0.0784` n `6`; index avg `-0.0364` n `25`; metal avg `0.4869` n `20`; unknown avg `-0.1501` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
