# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T09:22:30.958244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.0391` n `229`; crypto_major avg `-0.0157` n `8`; equity avg `-0.0426` n `91`; fx avg `-0.0038` n `6`; index avg `0.0053` n `25`; metal avg `0.0217` n `20`; unknown avg `-0.0239` n `763`
- 1h: commodity avg `0.0504` n `12`; crypto_alt avg `-0.0626` n `229`; crypto_major avg `0.0075` n `8`; equity avg `-0.1626` n `91`; fx avg `-0.0008` n `6`; index avg `-0.0135` n `25`; metal avg `-0.051` n `20`; unknown avg `2.8475` n `759`
- 4h: commodity avg `0.2671` n `12`; crypto_alt avg `0.5544` n `229`; crypto_major avg `0.7162` n `8`; equity avg `0.5093` n `91`; fx avg `-0.0488` n `6`; index avg `0.111` n `25`; metal avg `0.1909` n `20`; unknown avg `4.0309` n `743`
- 24h: commodity avg `0.4464` n `12`; crypto_alt avg `0.6484` n `229`; crypto_major avg `0.0643` n `8`; equity avg `-1.4609` n `90`; fx avg `-0.0743` n `6`; index avg `-0.3493` n `25`; metal avg `-0.3284` n `20`; unknown avg `-0.4157` n `741`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
