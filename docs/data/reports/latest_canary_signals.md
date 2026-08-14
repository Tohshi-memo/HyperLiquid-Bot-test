# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T23:42:19.428615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `12`; crypto_alt avg `0.1083` n `230`; crypto_major avg `0.2038` n `8`; equity avg `-0.0118` n `114`; fx avg `-0.0751` n `6`; index avg `0.0014` n `25`; metal avg `0.0155` n `20`; unknown avg `0.2554` n `791`
- 1h: commodity avg `0.0292` n `12`; crypto_alt avg `0.2085` n `230`; crypto_major avg `0.3054` n `8`; equity avg `0.0118` n `114`; fx avg `-0.0663` n `6`; index avg `-0.0008` n `25`; metal avg `0.0253` n `20`; unknown avg `0.1398` n `791`
- 4h: commodity avg `0.0643` n `12`; crypto_alt avg `0.4349` n `230`; crypto_major avg `0.4217` n `8`; equity avg `0.2167` n `114`; fx avg `-0.0633` n `6`; index avg `0.0228` n `25`; metal avg `0.0264` n `20`; unknown avg `0.7788` n `791`
- 24h: commodity avg `0.2368` n `12`; crypto_alt avg `0.2752` n `230`; crypto_major avg `-0.6529` n `8`; equity avg `-0.5139` n `114`; fx avg `0.0098` n `6`; index avg `-0.1061` n `25`; metal avg `0.2121` n `20`; unknown avg `-0.1465` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
