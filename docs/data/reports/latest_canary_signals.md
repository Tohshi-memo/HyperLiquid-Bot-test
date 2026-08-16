# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T03:07:29.806242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `0.208` n `230`; crypto_major avg `0.0828` n `8`; equity avg `-0.0008` n `114`; fx avg `-0.0016` n `6`; index avg `-0.0025` n `25`; metal avg `0.0143` n `20`; unknown avg `0.0826` n `791`
- 1h: commodity avg `-0.0238` n `12`; crypto_alt avg `0.1989` n `230`; crypto_major avg `0.1847` n `8`; equity avg `0.0382` n `114`; fx avg `-0.0021` n `6`; index avg `0.003` n `25`; metal avg `0.0206` n `20`; unknown avg `0.0076` n `791`
- 4h: commodity avg `0.0492` n `12`; crypto_alt avg `-0.3021` n `230`; crypto_major avg `0.0204` n `8`; equity avg `0.0544` n `114`; fx avg `-0.0043` n `6`; index avg `0.0102` n `25`; metal avg `0.0289` n `20`; unknown avg `-0.0704` n `791`
- 24h: commodity avg `-0.0272` n `12`; crypto_alt avg `-0.071` n `230`; crypto_major avg `-0.0811` n `8`; equity avg `0.1939` n `114`; fx avg `-0.0555` n `6`; index avg `0.011` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.0052` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2233`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
