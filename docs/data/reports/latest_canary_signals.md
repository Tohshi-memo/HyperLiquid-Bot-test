# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T10:22:37.597340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `13`; crypto_alt avg `-0.0385` n `238`; crypto_major avg `-0.0569` n `8`; equity avg `-0.0249` n `154`; fx avg `-0.0011` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0396` n `20`; unknown avg `-0.0198` n `1236`
- 1h: commodity avg `-0.0509` n `13`; crypto_alt avg `-0.6508` n `238`; crypto_major avg `-0.4095` n `8`; equity avg `-0.102` n `154`; fx avg `0.0268` n `6`; index avg `-0.049` n `27`; metal avg `-0.0004` n `20`; unknown avg `5.8398` n `1234`
- 4h: commodity avg `0.1477` n `13`; crypto_alt avg `-0.5196` n `237`; crypto_major avg `-0.2846` n `8`; equity avg `0.2748` n `154`; fx avg `0.0024` n `6`; index avg `0.0508` n `27`; metal avg `-0.0208` n `20`; unknown avg `72.0173` n `1190`
- 24h: commodity avg `0.144` n `13`; crypto_alt avg `-0.955` n `237`; crypto_major avg `-0.5799` n `8`; equity avg `0.6672` n `153`; fx avg `-0.0341` n `6`; index avg `0.293` n `27`; metal avg `-0.3718` n `20`; unknown avg `1047.5121` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
