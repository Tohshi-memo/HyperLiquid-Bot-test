# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T03:52:34.043940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `-0.2123` n `229`; crypto_major avg `-0.2126` n `8`; equity avg `-0.2769` n `91`; fx avg `-0.0008` n `6`; index avg `-0.0683` n `25`; metal avg `-0.0721` n `20`; unknown avg `-0.2189` n `763`
- 1h: commodity avg `-0.0551` n `12`; crypto_alt avg `-0.3076` n `229`; crypto_major avg `-0.2837` n `8`; equity avg `-0.4543` n `91`; fx avg `-0.0433` n `6`; index avg `-0.109` n `25`; metal avg `-0.1302` n `20`; unknown avg `0.79` n `763`
- 4h: commodity avg `-0.0242` n `12`; crypto_alt avg `-1.2347` n `229`; crypto_major avg `-1.1982` n `8`; equity avg `-1.2484` n `91`; fx avg `-0.1076` n `6`; index avg `-0.3724` n `25`; metal avg `-0.3629` n `20`; unknown avg `1.1652` n `761`
- 24h: commodity avg `0.277` n `12`; crypto_alt avg `-0.3993` n `229`; crypto_major avg `-0.8625` n `8`; equity avg `-1.441` n `90`; fx avg `-0.0311` n `6`; index avg `-0.2698` n `25`; metal avg `-0.3341` n `20`; unknown avg `-0.4781` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
