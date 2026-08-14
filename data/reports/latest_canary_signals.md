# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T18:37:33.215769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.103` n `230`; crypto_major avg `-0.075` n `8`; equity avg `-0.0766` n `114`; fx avg `0.0127` n `6`; index avg `-0.0099` n `25`; metal avg `-0.0033` n `20`; unknown avg `-0.0396` n `791`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.1616` n `230`; crypto_major avg `-0.3036` n `8`; equity avg `-0.1338` n `114`; fx avg `-0.0002` n `6`; index avg `0.004` n `25`; metal avg `-0.0295` n `20`; unknown avg `1.7754` n `791`
- 4h: commodity avg `0.0855` n `12`; crypto_alt avg `0.5937` n `230`; crypto_major avg `0.0939` n `8`; equity avg `-0.7062` n `114`; fx avg `0.0575` n `6`; index avg `-0.0923` n `25`; metal avg `-0.0584` n `20`; unknown avg `37.7479` n `787`
- 24h: commodity avg `0.2801` n `12`; crypto_alt avg `0.5742` n `230`; crypto_major avg `-0.6431` n `8`; equity avg `-0.6847` n `114`; fx avg `0.0722` n `6`; index avg `-0.1127` n `25`; metal avg `0.1258` n `20`; unknown avg `0.1177` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
