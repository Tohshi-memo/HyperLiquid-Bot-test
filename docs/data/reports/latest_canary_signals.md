# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T20:37:36.761019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `13`; crypto_alt avg `-0.0315` n `237`; crypto_major avg `-0.0821` n `8`; equity avg `0.05` n `154`; fx avg `-0.0082` n `6`; index avg `0.0046` n `27`; metal avg `-0.0031` n `20`; unknown avg `10.706` n `1230`
- 1h: commodity avg `-0.133` n `13`; crypto_alt avg `-0.2143` n `237`; crypto_major avg `-0.3896` n `8`; equity avg `-0.1734` n `154`; fx avg `-0.0165` n `6`; index avg `-0.0211` n `27`; metal avg `-0.002` n `20`; unknown avg `9.5657` n `1142`
- 4h: commodity avg `-0.4489` n `13`; crypto_alt avg `-0.0906` n `237`; crypto_major avg `-0.0222` n `8`; equity avg `-0.0577` n `154`; fx avg `-0.0386` n `6`; index avg `-0.0212` n `27`; metal avg `-0.0705` n `20`; unknown avg `8.9195` n `1142`
- 24h: commodity avg `-0.309` n `13`; crypto_alt avg `-0.7411` n `237`; crypto_major avg `-0.4998` n `8`; equity avg `0.4281` n `153`; fx avg `0.0195` n `6`; index avg `-0.1134` n `27`; metal avg `0.0025` n `20`; unknown avg `741.4069` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
