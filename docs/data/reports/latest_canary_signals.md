# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T11:07:37.587202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1176` n `13`; crypto_alt avg `0.2682` n `238`; crypto_major avg `0.1141` n `8`; equity avg `0.3368` n `154`; fx avg `-0.0053` n `6`; index avg `0.0553` n `27`; metal avg `0.0343` n `20`; unknown avg `0.5895` n `1210`
- 1h: commodity avg `-0.3124` n `13`; crypto_alt avg `0.8755` n `238`; crypto_major avg `0.691` n `8`; equity avg `0.7901` n `154`; fx avg `-0.0198` n `6`; index avg `0.1368` n `27`; metal avg `0.0766` n `20`; unknown avg `2.9124` n `1210`
- 4h: commodity avg `-0.3436` n `13`; crypto_alt avg `0.4658` n `238`; crypto_major avg `0.5504` n `8`; equity avg `1.38` n `154`; fx avg `0.006` n `6`; index avg `0.2126` n `27`; metal avg `0.1749` n `20`; unknown avg `74.7747` n `1176`
- 24h: commodity avg `-0.219` n `13`; crypto_alt avg `0.1912` n `237`; crypto_major avg `0.279` n `8`; equity avg `1.7992` n `153`; fx avg `-0.0588` n `6`; index avg `0.479` n `27`; metal avg `-0.1865` n `20`; unknown avg `1050.758` n `1040`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
