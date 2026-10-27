# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T03:37:26.332358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0351` n `13`; crypto_alt avg `0.3238` n `237`; crypto_major avg `0.2521` n `8`; equity avg `0.1366` n `154`; fx avg `-0.0007` n `6`; index avg `0.0305` n `27`; metal avg `0.0823` n `20`; unknown avg `1.3137` n `1234`
- 1h: commodity avg `0.0286` n `13`; crypto_alt avg `-0.0206` n `237`; crypto_major avg `0.0371` n `8`; equity avg `-0.0745` n `154`; fx avg `0.0242` n `6`; index avg `-0.0037` n `27`; metal avg `-0.029` n `20`; unknown avg `1.5777` n `1228`
- 4h: commodity avg `-0.0595` n `13`; crypto_alt avg `-0.6414` n `237`; crypto_major avg `-0.243` n `8`; equity avg `-0.0101` n `154`; fx avg `0.0245` n `6`; index avg `0.0481` n `27`; metal avg `-0.0407` n `20`; unknown avg `1.1079` n `1220`
- 24h: commodity avg `0.1527` n `13`; crypto_alt avg `0.4541` n `237`; crypto_major avg `0.881` n `8`; equity avg `1.7741` n `153`; fx avg `0.0278` n `6`; index avg `0.0855` n `27`; metal avg `-0.1207` n `20`; unknown avg `1005.2315` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
