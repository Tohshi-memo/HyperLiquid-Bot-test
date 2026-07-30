# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T09:22:29.309501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0843` n `12`; crypto_alt avg `0.0278` n `230`; crypto_major avg `0.0932` n `8`; equity avg `0.2365` n `102`; fx avg `0.0215` n `6`; index avg `0.0576` n `25`; metal avg `0.0499` n `20`; unknown avg `-0.0276` n `779`
- 1h: commodity avg `-0.2181` n `12`; crypto_alt avg `0.2487` n `230`; crypto_major avg `0.4215` n `8`; equity avg `0.499` n `102`; fx avg `0.0317` n `6`; index avg `0.066` n `25`; metal avg `0.1524` n `20`; unknown avg `0.0324` n `771`
- 4h: commodity avg `-0.1729` n `12`; crypto_alt avg `0.4396` n `230`; crypto_major avg `0.6955` n `8`; equity avg `0.7336` n `102`; fx avg `0.0346` n `6`; index avg `0.0449` n `25`; metal avg `0.319` n `20`; unknown avg `0.0209` n `739`
- 24h: commodity avg `0.6272` n `12`; crypto_alt avg `-0.3116` n `230`; crypto_major avg `-0.2571` n `8`; equity avg `-3.0895` n `102`; fx avg `0.0044` n `6`; index avg `-0.4238` n `25`; metal avg `0.2755` n `20`; unknown avg `-0.1578` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
