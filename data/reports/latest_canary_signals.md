# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T01:52:27.134315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `12`; crypto_alt avg `-0.0603` n `230`; crypto_major avg `-0.0377` n `8`; equity avg `0.0094` n `114`; fx avg `0.0049` n `6`; index avg `0.0001` n `25`; metal avg `-0.0077` n `20`; unknown avg `0.1366` n `791`
- 1h: commodity avg `-0.0481` n `12`; crypto_alt avg `-0.1898` n `230`; crypto_major avg `0.0383` n `8`; equity avg `0.0177` n `114`; fx avg `-0.0082` n `6`; index avg `0.0024` n `25`; metal avg `-0.0296` n `20`; unknown avg `0.3382` n `791`
- 4h: commodity avg `0.0097` n `12`; crypto_alt avg `0.2748` n `230`; crypto_major avg `0.3942` n `8`; equity avg `0.0126` n `114`; fx avg `-0.0171` n `6`; index avg `-0.0091` n `25`; metal avg `0.0363` n `20`; unknown avg `0.6028` n `791`
- 24h: commodity avg `0.2293` n `12`; crypto_alt avg `-0.1469` n `230`; crypto_major avg `-0.6724` n `8`; equity avg `-0.1884` n `114`; fx avg `0.1143` n `6`; index avg `-0.0287` n `25`; metal avg `0.503` n `20`; unknown avg `-0.0853` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
