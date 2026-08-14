# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T22:22:27.483506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `0.0053` n `230`; crypto_major avg `-0.0526` n `8`; equity avg `0.0157` n `114`; fx avg `-0.0036` n `6`; index avg `0.0002` n `25`; metal avg `-0.005` n `20`; unknown avg `0.0936` n `791`
- 1h: commodity avg `0.062` n `12`; crypto_alt avg `0.1205` n `230`; crypto_major avg `0.0356` n `8`; equity avg `0.0769` n `114`; fx avg `0.002` n `6`; index avg `0.0031` n `25`; metal avg `0.0069` n `20`; unknown avg `0.2819` n `791`
- 4h: commodity avg `0.0004` n `12`; crypto_alt avg `-0.0483` n `230`; crypto_major avg `-0.0492` n `8`; equity avg `0.223` n `114`; fx avg `0.0264` n `6`; index avg `0.0293` n `25`; metal avg `0.0259` n `20`; unknown avg `8.6471` n `791`
- 24h: commodity avg `0.2625` n `12`; crypto_alt avg `0.1457` n `230`; crypto_major avg `-1.1392` n `8`; equity avg `-0.5118` n `114`; fx avg `0.0815` n `6`; index avg `-0.0928` n `25`; metal avg `0.2568` n `20`; unknown avg `-0.124` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
