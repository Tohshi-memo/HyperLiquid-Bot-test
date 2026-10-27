# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T21:07:27.765730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `13`; crypto_alt avg `-0.0157` n `238`; crypto_major avg `0.0221` n `8`; equity avg `0.061` n `154`; fx avg `0.0066` n `6`; index avg `0.0035` n `27`; metal avg `-0.0024` n `20`; unknown avg `1.3826` n `1224`
- 1h: commodity avg `0.0085` n `13`; crypto_alt avg `-0.0924` n `238`; crypto_major avg `-0.0988` n `8`; equity avg `-0.0717` n `154`; fx avg `-0.0099` n `6`; index avg `-0.0172` n `27`; metal avg `0.0052` n `20`; unknown avg `5.2803` n `1168`
- 4h: commodity avg `0.1021` n `13`; crypto_alt avg `0.1207` n `238`; crypto_major avg `0.0115` n `8`; equity avg `-0.1913` n `154`; fx avg `-0.0161` n `6`; index avg `0.0068` n `27`; metal avg `0.0286` n `20`; unknown avg `2.582` n `1154`
- 24h: commodity avg `-0.2195` n `13`; crypto_alt avg `1.4935` n `237`; crypto_major avg `1.7092` n `8`; equity avg `1.5282` n `154`; fx avg `-0.0487` n `6`; index avg `0.41` n `27`; metal avg `0.2091` n `20`; unknown avg `24.5813` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2333`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1989`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
