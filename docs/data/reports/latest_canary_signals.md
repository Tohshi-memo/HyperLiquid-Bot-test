# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T05:52:26.553894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.0088` n `230`; crypto_major avg `-0.0006` n `8`; equity avg `-0.0313` n `92`; fx avg `0.0023` n `6`; index avg `-0.0053` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.0466` n `765`
- 1h: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.0474` n `230`; crypto_major avg `-0.0546` n `8`; equity avg `-0.0496` n `92`; fx avg `0.0048` n `6`; index avg `-0.0108` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.3185` n `765`
- 4h: commodity avg `-0.1124` n `12`; crypto_alt avg `0.0194` n `230`; crypto_major avg `-0.2256` n `8`; equity avg `-0.0321` n `92`; fx avg `0.0018` n `6`; index avg `-0.0093` n `25`; metal avg `-0.0112` n `20`; unknown avg `-0.4091` n `765`
- 24h: commodity avg `0.4809` n `12`; crypto_alt avg `-0.413` n `230`; crypto_major avg `-0.5308` n `8`; equity avg `0.0386` n `92`; fx avg `-0.0096` n `6`; index avg `-0.0913` n `25`; metal avg `-0.0973` n `20`; unknown avg `-0.0536` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
