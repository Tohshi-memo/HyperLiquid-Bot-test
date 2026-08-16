# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T05:49:06.864537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0105` n `12`; crypto_alt avg `0.0059` n `230`; crypto_major avg `-0.0368` n `8`; equity avg `0.0239` n `114`; fx avg `0.0037` n `6`; index avg `-0.0016` n `25`; metal avg `0.0016` n `20`; unknown avg `0.0703` n `791`
- 1h: commodity avg `-0.017` n `12`; crypto_alt avg `-0.0398` n `230`; crypto_major avg `-0.1363` n `8`; equity avg `0.0196` n `114`; fx avg `0.0035` n `6`; index avg `0.0052` n `25`; metal avg `0.0173` n `20`; unknown avg `0.3929` n `791`
- 4h: commodity avg `-0.06` n `12`; crypto_alt avg `0.0317` n `230`; crypto_major avg `-0.0286` n `8`; equity avg `0.1828` n `114`; fx avg `0.0008` n `6`; index avg `0.0133` n `25`; metal avg `0.0301` n `20`; unknown avg `0.0247` n `791`
- 24h: commodity avg `-0.1099` n `12`; crypto_alt avg `-0.2726` n `230`; crypto_major avg `-0.0711` n `8`; equity avg `0.3495` n `114`; fx avg `-0.0116` n `6`; index avg `0.0493` n `25`; metal avg `0.0347` n `20`; unknown avg `-0.0095` n `765`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2203`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
