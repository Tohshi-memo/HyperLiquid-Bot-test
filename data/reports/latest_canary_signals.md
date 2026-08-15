# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T06:22:25.115789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.0589` n `230`; crypto_major avg `0.0003` n `8`; equity avg `-0.0106` n `114`; fx avg `-0.0096` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0068` n `20`; unknown avg `1.9679` n `791`
- 1h: commodity avg `0.0104` n `12`; crypto_alt avg `-0.0828` n `230`; crypto_major avg `-0.0749` n `8`; equity avg `-0.0604` n `114`; fx avg `-0.0053` n `6`; index avg `-0.0176` n `25`; metal avg `-0.0166` n `20`; unknown avg `-0.0198` n `759`
- 4h: commodity avg `0.0463` n `12`; crypto_alt avg `0.2519` n `230`; crypto_major avg `-0.1028` n `8`; equity avg `-0.0517` n `114`; fx avg `0.0562` n `6`; index avg `-0.0249` n `25`; metal avg `-0.0378` n `20`; unknown avg `-0.0527` n `759`
- 24h: commodity avg `0.0441` n `12`; crypto_alt avg `0.8704` n `230`; crypto_major avg `-0.0934` n `8`; equity avg `-0.0481` n `114`; fx avg `0.1452` n `6`; index avg `-0.0781` n `25`; metal avg `0.2912` n `20`; unknown avg `-0.1681` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
