# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T00:52:27.810267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `0.0341` n `230`; crypto_major avg `0.0016` n `8`; equity avg `0.021` n `114`; fx avg `0.0056` n `6`; index avg `0.0033` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.0854` n `791`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `0.0829` n `230`; crypto_major avg `-0.0351` n `8`; equity avg `-0.0079` n `114`; fx avg `0.0057` n `6`; index avg `-0.0021` n `25`; metal avg `0.0387` n `20`; unknown avg `-0.06` n `791`
- 4h: commodity avg `0.0654` n `12`; crypto_alt avg `0.4409` n `230`; crypto_major avg `0.3805` n `8`; equity avg `0.0119` n `114`; fx avg `-0.0247` n `6`; index avg `0.0` n `25`; metal avg `0.1004` n `20`; unknown avg `2.7331` n `791`
- 24h: commodity avg `0.2551` n `12`; crypto_alt avg `0.1346` n `230`; crypto_major avg `-0.7526` n `8`; equity avg `-0.3883` n `114`; fx avg `0.0897` n `6`; index avg `-0.0702` n `25`; metal avg `0.4338` n `20`; unknown avg `-0.3009` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
