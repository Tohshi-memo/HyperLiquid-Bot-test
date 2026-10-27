# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T12:07:34.559782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `13`; crypto_alt avg `-0.1434` n `238`; crypto_major avg `-0.0609` n `8`; equity avg `-0.0434` n `154`; fx avg `0.0228` n `6`; index avg `0.0067` n `27`; metal avg `-0.0023` n `20`; unknown avg `0.9034` n `1226`
- 1h: commodity avg `0.1485` n `13`; crypto_alt avg `-0.543` n `238`; crypto_major avg `-0.2583` n `8`; equity avg `-0.1799` n `154`; fx avg `0.0351` n `6`; index avg `-0.0315` n `27`; metal avg `-0.0331` n `20`; unknown avg `8.0452` n `1206`
- 4h: commodity avg `-0.2961` n `13`; crypto_alt avg `-0.515` n `238`; crypto_major avg `-0.0733` n `8`; equity avg `0.9369` n `154`; fx avg `0.0053` n `6`; index avg `0.1628` n `27`; metal avg `0.1309` n `20`; unknown avg `15.2882` n `1172`
- 24h: commodity avg `-0.0972` n `13`; crypto_alt avg `-0.7533` n `237`; crypto_major avg `-0.2879` n `8`; equity avg `0.6964` n `153`; fx avg `-0.0212` n `6`; index avg `0.3037` n `27`; metal avg `-0.3032` n `20`; unknown avg `1020.1351` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
