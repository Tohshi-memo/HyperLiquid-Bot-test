# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T19:52:30.573380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0784` n `13`; crypto_alt avg `-0.1471` n `237`; crypto_major avg `-0.1549` n `8`; equity avg `-0.2692` n `154`; fx avg `0.0029` n `6`; index avg `-0.0269` n `27`; metal avg `0.0002` n `20`; unknown avg `145.2565` n `1238`
- 1h: commodity avg `-0.0133` n `13`; crypto_alt avg `0.0687` n `237`; crypto_major avg `0.0147` n `8`; equity avg `-0.3469` n `154`; fx avg `-0.0028` n `6`; index avg `-0.0268` n `27`; metal avg `-0.0217` n `20`; unknown avg `86.8231` n `1236`
- 4h: commodity avg `-0.2995` n `13`; crypto_alt avg `-0.9799` n `237`; crypto_major avg `-0.5123` n `8`; equity avg `-0.303` n `154`; fx avg `-0.0175` n `6`; index avg `-0.0416` n `27`; metal avg `-0.099` n `20`; unknown avg `7.0633` n `1230`
- 24h: commodity avg `-0.2348` n `13`; crypto_alt avg `-0.7172` n `237`; crypto_major avg `-0.2979` n `8`; equity avg `0.3294` n `153`; fx avg `0.0359` n `6`; index avg `-0.1239` n `27`; metal avg `0.0127` n `20`; unknown avg `760.5216` n `948`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
