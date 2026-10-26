# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T17:07:53.865889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1086` n `13`; crypto_alt avg `0.579` n `237`; crypto_major avg `0.5486` n `8`; equity avg `0.3265` n `154`; fx avg `-0.0194` n `6`; index avg `0.0558` n `27`; metal avg `0.0808` n `20`; unknown avg `0.4931` n `1236`
- 1h: commodity avg `-0.1168` n `13`; crypto_alt avg `-0.026` n `237`; crypto_major avg `0.1126` n `8`; equity avg `0.1723` n `154`; fx avg `-0.0239` n `6`; index avg `0.0147` n `27`; metal avg `0.0438` n `20`; unknown avg `0.156` n `1238`
- 4h: commodity avg `0.1963` n `13`; crypto_alt avg `0.5536` n `237`; crypto_major avg `0.559` n `8`; equity avg `1.2456` n `153`; fx avg `0.0039` n `6`; index avg `0.1876` n `27`; metal avg `0.1093` n `20`; unknown avg `596.7968` n `1162`
- 24h: commodity avg `-0.0316` n `13`; crypto_alt avg `-0.2694` n `237`; crypto_major avg `-0.0379` n `8`; equity avg `0.782` n `153`; fx avg `0.0454` n `6`; index avg `-0.0629` n `27`; metal avg `0.1494` n `20`; unknown avg `791.5001` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
