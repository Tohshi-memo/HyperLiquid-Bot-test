# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T19:22:30.992024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0635` n `13`; crypto_alt avg `-0.0503` n `238`; crypto_major avg `-0.1159` n `8`; equity avg `-0.0309` n `154`; fx avg `0.0047` n `6`; index avg `0.0034` n `27`; metal avg `0.0238` n `20`; unknown avg `92.2046` n `1236`
- 1h: commodity avg `-0.0216` n `13`; crypto_alt avg `0.091` n `238`; crypto_major avg `0.0779` n `8`; equity avg `0.2306` n `154`; fx avg `0.0111` n `6`; index avg `0.0304` n `27`; metal avg `0.0693` n `20`; unknown avg `7.5286` n `1234`
- 4h: commodity avg `-0.0177` n `13`; crypto_alt avg `0.3536` n `238`; crypto_major avg `0.3027` n `8`; equity avg `0.537` n `154`; fx avg `-0.0046` n `6`; index avg `0.0568` n `27`; metal avg `0.0035` n `20`; unknown avg `5.5927` n `1226`
- 24h: commodity avg `-0.546` n `13`; crypto_alt avg `0.8388` n `237`; crypto_major avg `1.0047` n `8`; equity avg `1.5165` n `154`; fx avg `-0.0473` n `6`; index avg `0.3954` n `27`; metal avg `0.1905` n `20`; unknown avg `28.4293` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2292`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
