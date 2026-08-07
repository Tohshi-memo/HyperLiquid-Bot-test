# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T00:37:36.355575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `0.0904` n `230`; crypto_major avg `0.0739` n `8`; equity avg `0.0879` n `112`; fx avg `-0.0075` n `6`; index avg `0.0242` n `25`; metal avg `-0.0252` n `20`; unknown avg `0.0813` n `782`
- 1h: commodity avg `0.0567` n `12`; crypto_alt avg `0.3037` n `230`; crypto_major avg `0.1498` n `8`; equity avg `-0.2357` n `112`; fx avg `-0.0007` n `6`; index avg `-0.056` n `25`; metal avg `-0.0705` n `20`; unknown avg `-0.0116` n `782`
- 4h: commodity avg `0.1453` n `12`; crypto_alt avg `0.2565` n `230`; crypto_major avg `-0.0959` n `8`; equity avg `0.2721` n `112`; fx avg `-0.0106` n `6`; index avg `-0.0252` n `25`; metal avg `-0.0688` n `20`; unknown avg `-0.0885` n `782`
- 24h: commodity avg `0.6995` n `12`; crypto_alt avg `0.13` n `230`; crypto_major avg `-1.2153` n `8`; equity avg `0.6446` n `109`; fx avg `0.0337` n `6`; index avg `-0.1081` n `25`; metal avg `-0.3136` n `20`; unknown avg `112.9613` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
