# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T15:52:36.603731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.0121` n `230`; crypto_major avg `0.0302` n `8`; equity avg `0.0042` n `114`; fx avg `0.0` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0145` n `791`
- 1h: commodity avg `0.0244` n `12`; crypto_alt avg `0.1048` n `230`; crypto_major avg `0.1152` n `8`; equity avg `0.0514` n `114`; fx avg `0.0074` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0162` n `791`
- 4h: commodity avg `-0.003` n `12`; crypto_alt avg `0.2092` n `230`; crypto_major avg `0.2109` n `8`; equity avg `0.0333` n `114`; fx avg `0.0016` n `6`; index avg `-0.0051` n `25`; metal avg `-0.0096` n `20`; unknown avg `0.0268` n `791`
- 24h: commodity avg `0.0543` n `12`; crypto_alt avg `-0.2111` n `230`; crypto_major avg `0.0611` n `8`; equity avg `0.3115` n `114`; fx avg `-0.0071` n `6`; index avg `0.0222` n `25`; metal avg `0.0342` n `20`; unknown avg `0.182` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2148`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
