# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T08:07:28.176980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.082` n `12`; crypto_alt avg `0.2071` n `230`; crypto_major avg `0.4482` n `8`; equity avg `-0.0464` n `121`; fx avg `-0.012` n `6`; index avg `-0.0116` n `25`; metal avg `-0.0234` n `20`; unknown avg `0.0396` n `793`
- 1h: commodity avg `0.1513` n `12`; crypto_alt avg `1.267` n `230`; crypto_major avg `0.7141` n `8`; equity avg `0.0839` n `121`; fx avg `-0.0521` n `6`; index avg `0.0142` n `25`; metal avg `0.0572` n `20`; unknown avg `0.1009` n `793`
- 4h: commodity avg `0.1543` n `12`; crypto_alt avg `2.5329` n `230`; crypto_major avg `1.6459` n `8`; equity avg `0.5196` n `121`; fx avg `-0.0111` n `6`; index avg `0.0579` n `25`; metal avg `0.1687` n `20`; unknown avg `0.0931` n `777`
- 24h: commodity avg `0.386` n `12`; crypto_alt avg `7.3274` n `230`; crypto_major avg `7.3329` n `8`; equity avg `0.1753` n `121`; fx avg `-0.068` n `6`; index avg `-0.0065` n `25`; metal avg `0.7453` n `20`; unknown avg `2.3959` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
