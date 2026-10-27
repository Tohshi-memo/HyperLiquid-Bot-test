# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T18:52:51.235169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0712` n `13`; crypto_alt avg `-0.0531` n `238`; crypto_major avg `-0.0427` n `8`; equity avg `0.043` n `154`; fx avg `-0.0077` n `6`; index avg `0.0004` n `27`; metal avg `-0.0065` n `20`; unknown avg `1.4481` n `1238`
- 1h: commodity avg `-0.0114` n `13`; crypto_alt avg `0.2754` n `238`; crypto_major avg `0.1083` n `8`; equity avg `0.0185` n `154`; fx avg `-0.0095` n `6`; index avg `-0.0163` n `27`; metal avg `-0.0334` n `20`; unknown avg `2.0239` n `1234`
- 4h: commodity avg `-0.0455` n `13`; crypto_alt avg `0.8389` n `238`; crypto_major avg `0.7243` n `8`; equity avg `0.6411` n `154`; fx avg `-0.0179` n `6`; index avg `0.0973` n `27`; metal avg `-0.0188` n `20`; unknown avg `8.5924` n `1196`
- 24h: commodity avg `-0.4663` n `13`; crypto_alt avg `1.2967` n `237`; crypto_major avg `1.3239` n `8`; equity avg `1.4524` n `154`; fx avg `-0.0668` n `6`; index avg `0.3813` n `27`; metal avg `0.1066` n `20`; unknown avg `26.1533` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
