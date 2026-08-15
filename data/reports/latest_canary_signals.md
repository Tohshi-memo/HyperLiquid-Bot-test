# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T05:07:26.020704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.1225` n `230`; crypto_major avg `0.0178` n `8`; equity avg `-0.0081` n `114`; fx avg `-0.0074` n `6`; index avg `0.0004` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.0821` n `791`
- 1h: commodity avg `0.0306` n `12`; crypto_alt avg `0.2133` n `230`; crypto_major avg `0.0289` n `8`; equity avg `-0.035` n `114`; fx avg `-0.0082` n `6`; index avg `-0.0144` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.1796` n `791`
- 4h: commodity avg `0.0218` n `12`; crypto_alt avg `0.307` n `230`; crypto_major avg `0.3026` n `8`; equity avg `0.0831` n `114`; fx avg `0.0449` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0483` n `20`; unknown avg `0.0749` n `791`
- 24h: commodity avg `0.1901` n `12`; crypto_alt avg `0.6615` n `230`; crypto_major avg `-0.1665` n `8`; equity avg `0.0045` n `114`; fx avg `0.1415` n `6`; index avg `-0.0133` n `25`; metal avg `0.457` n `20`; unknown avg `0.1381` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
