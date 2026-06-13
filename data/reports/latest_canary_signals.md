# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T05:37:28.510084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `-0.0608` n `228`; crypto_major avg `0.0227` n `8`; equity avg `0.0109` n `74`; fx avg `-0.003` n `6`; index avg `0.0078` n `23`; metal avg `-0.0036` n `18`; unknown avg `-0.3703` n `643`
- 1h: commodity avg `-0.0434` n `12`; crypto_alt avg `-0.4305` n `228`; crypto_major avg `-0.3626` n `8`; equity avg `-0.0554` n `74`; fx avg `0.0215` n `6`; index avg `0.0805` n `23`; metal avg `0.0064` n `18`; unknown avg `-0.0229` n `635`
- 4h: commodity avg `-0.0807` n `12`; crypto_alt avg `-0.6245` n `228`; crypto_major avg `-0.7327` n `8`; equity avg `-0.2181` n `74`; fx avg `0.0297` n `6`; index avg `0.1883` n `23`; metal avg `-0.0753` n `18`; unknown avg `-0.1921` n `635`
- 24h: commodity avg `-0.4475` n `12`; crypto_alt avg `0.0169` n `228`; crypto_major avg `-0.4463` n `8`; equity avg `-0.6858` n `74`; fx avg `0.0296` n `6`; index avg `0.7837` n `23`; metal avg `0.716` n `18`; unknown avg `40.4437` n `507`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
