# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T15:22:34.003720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0924` n `13`; crypto_alt avg `-0.0522` n `237`; crypto_major avg `0.1008` n `8`; equity avg `0.2664` n `153`; fx avg `-0.0017` n `6`; index avg `0.0113` n `26`; metal avg `-0.0046` n `20`; unknown avg `1.53` n `1236`
- 1h: commodity avg `0.1918` n `13`; crypto_alt avg `1.3649` n `237`; crypto_major avg `1.2291` n `8`; equity avg `2.0874` n `153`; fx avg `0.0313` n `6`; index avg `0.2834` n `26`; metal avg `0.2725` n `20`; unknown avg `633.7287` n `1174`
- 4h: commodity avg `0.0964` n `13`; crypto_alt avg `1.2726` n `237`; crypto_major avg `0.9219` n `8`; equity avg `2.0325` n `152`; fx avg `0.0177` n `6`; index avg `0.3325` n `26`; metal avg `0.1419` n `20`; unknown avg `630.6302` n `1156`
- 24h: commodity avg `-0.2023` n `13`; crypto_alt avg `0.9529` n `237`; crypto_major avg `0.7637` n `8`; equity avg `1.2103` n `152`; fx avg `0.0632` n `6`; index avg `0.2634` n `26`; metal avg `0.2175` n `20`; unknown avg `806.6388` n `926`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2304`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
