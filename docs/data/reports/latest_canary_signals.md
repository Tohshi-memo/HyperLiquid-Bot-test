# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T20:37:38.532934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `13`; crypto_alt avg `-0.1245` n `238`; crypto_major avg `-0.1367` n `8`; equity avg `-0.13` n `154`; fx avg `-0.0008` n `6`; index avg `-0.0071` n `27`; metal avg `0.0029` n `20`; unknown avg `0.953` n `1232`
- 1h: commodity avg `0.1139` n `13`; crypto_alt avg `-0.1726` n `238`; crypto_major avg `-0.2194` n `8`; equity avg `-0.4409` n `154`; fx avg `-0.0148` n `6`; index avg `-0.0428` n `27`; metal avg `-0.0072` n `20`; unknown avg `2.5321` n `1158`
- 4h: commodity avg `0.1563` n `13`; crypto_alt avg `0.0286` n `238`; crypto_major avg `-0.0513` n `8`; equity avg `-0.378` n `154`; fx avg `-0.0094` n `6`; index avg `-0.0407` n `27`; metal avg `0.021` n `20`; unknown avg `2.2212` n `1158`
- 24h: commodity avg `-0.2149` n `13`; crypto_alt avg `1.1566` n `237`; crypto_major avg `1.4404` n `8`; equity avg `1.453` n `154`; fx avg `-0.0487` n `6`; index avg `0.4136` n `27`; metal avg `0.2161` n `20`; unknown avg `25.5219` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2331`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1987`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
