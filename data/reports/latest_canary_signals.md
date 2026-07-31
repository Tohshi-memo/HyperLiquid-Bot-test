# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T21:33:16.908379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1399` n `12`; crypto_alt avg `-0.0726` n `230`; crypto_major avg `-0.1367` n `8`; equity avg `0.0021` n `102`; fx avg `0.011` n `6`; index avg `-0.037` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0547` n `781`
- 1h: commodity avg `0.653` n `12`; crypto_alt avg `-0.1316` n `230`; crypto_major avg `-0.1614` n `8`; equity avg `-0.1631` n `102`; fx avg `-0.0132` n `6`; index avg `-0.0816` n `25`; metal avg `-0.0632` n `20`; unknown avg `0.5611` n `780`
- 4h: commodity avg `0.7369` n `12`; crypto_alt avg `-0.5207` n `230`; crypto_major avg `-0.5986` n `8`; equity avg `-1.0516` n `102`; fx avg `-0.0052` n `6`; index avg `-0.1513` n `25`; metal avg `-0.0514` n `20`; unknown avg `7.1728` n `780`
- 24h: commodity avg `0.8441` n `12`; crypto_alt avg `-0.6319` n `230`; crypto_major avg `-2.1621` n `8`; equity avg `-1.2643` n `102`; fx avg `0.1236` n `6`; index avg `0.06` n `25`; metal avg `-0.4321` n `20`; unknown avg `0.2597` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
