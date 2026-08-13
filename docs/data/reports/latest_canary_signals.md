# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T20:52:25.235165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `-0.032` n `230`; crypto_major avg `-0.1025` n `8`; equity avg `0.0143` n `113`; fx avg `-0.0003` n `6`; index avg `0.0012` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.1363` n `787`
- 1h: commodity avg `-0.0011` n `12`; crypto_alt avg `0.0005` n `230`; crypto_major avg `-0.012` n `8`; equity avg `0.1831` n `113`; fx avg `0.0075` n `6`; index avg `0.0345` n `25`; metal avg `-0.0091` n `20`; unknown avg `0.1457` n `787`
- 4h: commodity avg `-0.1735` n `12`; crypto_alt avg `0.3109` n `230`; crypto_major avg `0.3524` n `8`; equity avg `0.1293` n `113`; fx avg `0.0149` n `6`; index avg `0.0031` n `25`; metal avg `-0.1503` n `20`; unknown avg `0.1829` n `787`
- 24h: commodity avg `-0.4355` n `12`; crypto_alt avg `-0.3434` n `230`; crypto_major avg `0.1815` n `8`; equity avg `1.6133` n `113`; fx avg `0.0133` n `6`; index avg `0.3271` n `25`; metal avg `-0.5235` n `20`; unknown avg `0.0434` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.244`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
