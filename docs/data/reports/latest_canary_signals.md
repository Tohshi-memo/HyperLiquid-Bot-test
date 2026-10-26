# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T10:07:35.525967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0576` n `13`; crypto_alt avg `-0.1076` n `237`; crypto_major avg `-0.0948` n `8`; equity avg `-0.1309` n `152`; fx avg `-0.0002` n `6`; index avg `-0.0238` n `26`; metal avg `-0.0372` n `20`; unknown avg `1.8917` n `1238`
- 1h: commodity avg `0.1252` n `13`; crypto_alt avg `0.1581` n `237`; crypto_major avg `0.3081` n `8`; equity avg `0.2667` n `152`; fx avg `0.0021` n `6`; index avg `0.0165` n `26`; metal avg `0.0437` n `20`; unknown avg `2.3185` n `1240`
- 4h: commodity avg `0.2251` n `13`; crypto_alt avg `0.3686` n `237`; crypto_major avg `0.283` n `8`; equity avg `0.2333` n `152`; fx avg `-0.0045` n `6`; index avg `0.0627` n `26`; metal avg `0.0736` n `20`; unknown avg `9.9559` n `1142`
- 24h: commodity avg `-0.3875` n `13`; crypto_alt avg `0.4245` n `237`; crypto_major avg `0.4414` n `8`; equity avg `0.0027` n `152`; fx avg `0.0417` n `6`; index avg `0.0596` n `26`; metal avg `0.2295` n `20`; unknown avg `-0.0843` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2635`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2206`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
