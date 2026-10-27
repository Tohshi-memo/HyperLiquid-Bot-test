# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T10:37:32.710707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.031` n `13`; crypto_alt avg `0.1679` n `238`; crypto_major avg `0.1896` n `8`; equity avg `0.0276` n `154`; fx avg `-0.0017` n `6`; index avg `0.0108` n `27`; metal avg `0.0067` n `20`; unknown avg `1.0571` n `1238`
- 1h: commodity avg `-0.0727` n `13`; crypto_alt avg `-0.2731` n `238`; crypto_major avg `-0.0806` n `8`; equity avg `-0.0146` n `154`; fx avg `0.0256` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0094` n `20`; unknown avg `1.2341` n `1234`
- 4h: commodity avg `0.0758` n `13`; crypto_alt avg `-0.4209` n `237`; crypto_major avg `-0.1646` n `8`; equity avg `0.3182` n `154`; fx avg `-0.0047` n `6`; index avg `0.0339` n `27`; metal avg `0.0148` n `20`; unknown avg `73.0796` n `1190`
- 24h: commodity avg `0.1126` n `13`; crypto_alt avg `-0.8894` n `237`; crypto_major avg `-0.5119` n `8`; equity avg `0.6687` n `153`; fx avg `-0.0414` n `6`; index avg `0.3097` n `27`; metal avg `-0.3303` n `20`; unknown avg `1045.8628` n `1040`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
