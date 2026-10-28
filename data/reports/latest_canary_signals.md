# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T16:37:28.929335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0052` n `13`; crypto_alt avg `-0.0127` n `238`; crypto_major avg `0.0194` n `8`; equity avg `-0.0232` n `155`; fx avg `0.0108` n `6`; index avg `-0.017` n `27`; metal avg `0.0007` n `20`; unknown avg `-0.0115` n `1236`
- 1h: commodity avg `0.1558` n `13`; crypto_alt avg `-0.0515` n `238`; crypto_major avg `0.0249` n `8`; equity avg `0.0218` n `155`; fx avg `0.0386` n `6`; index avg `-0.0077` n `27`; metal avg `-0.0081` n `20`; unknown avg `1.3441` n `1226`
- 4h: commodity avg `0.2836` n `13`; crypto_alt avg `-0.1664` n `238`; crypto_major avg `-0.3497` n `8`; equity avg `-0.2203` n `155`; fx avg `0.1034` n `6`; index avg `0.0354` n `27`; metal avg `-0.1618` n `20`; unknown avg `1.6275` n `1150`
- 24h: commodity avg `0.7423` n `13`; crypto_alt avg `-0.1899` n `238`; crypto_major avg `-0.1873` n `8`; equity avg `0.9146` n `154`; fx avg `0.2647` n `6`; index avg `0.2067` n `27`; metal avg `-0.1769` n `20`; unknown avg `3.509` n `1100`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
