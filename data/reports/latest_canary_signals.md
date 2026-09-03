# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T05:37:30.702081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0813` n `12`; crypto_alt avg `0.2223` n `232`; crypto_major avg `0.3224` n `8`; equity avg `0.1792` n `133`; fx avg `-0.0097` n `6`; index avg `0.0473` n `26`; metal avg `0.0318` n `20`; unknown avg `0.2081` n `792`
- 1h: commodity avg `-0.1575` n `12`; crypto_alt avg `0.0026` n `232`; crypto_major avg `-0.0247` n `8`; equity avg `-0.6174` n `133`; fx avg `0.03` n `6`; index avg `-0.145` n `26`; metal avg `-0.1114` n `20`; unknown avg `7.961` n `790`
- 4h: commodity avg `-0.2184` n `12`; crypto_alt avg `0.3671` n `232`; crypto_major avg `0.2315` n `8`; equity avg `-0.3743` n `133`; fx avg `-0.0305` n `6`; index avg `-0.1237` n `26`; metal avg `0.0421` n `20`; unknown avg `2.7047` n `790`
- 24h: commodity avg `-0.0247` n `12`; crypto_alt avg `-0.0285` n `232`; crypto_major avg `-0.0788` n `8`; equity avg `0.7872` n `133`; fx avg `-0.3385` n `6`; index avg `0.0321` n `26`; metal avg `0.6735` n `20`; unknown avg `-0.0651` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
