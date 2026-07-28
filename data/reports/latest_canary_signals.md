# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T08:07:30.522988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0399` n `12`; crypto_alt avg `0.1479` n `230`; crypto_major avg `0.0344` n `8`; equity avg `-0.0862` n `102`; fx avg `0.0094` n `6`; index avg `-0.0129` n `25`; metal avg `0.0361` n `20`; unknown avg `-0.0279` n `774`
- 1h: commodity avg `-0.0666` n `12`; crypto_alt avg `-0.2423` n `230`; crypto_major avg `-0.11` n `8`; equity avg `-0.1229` n `102`; fx avg `-0.0002` n `6`; index avg `-0.0599` n `25`; metal avg `0.0273` n `20`; unknown avg `-0.0137` n `774`
- 4h: commodity avg `-0.2636` n `12`; crypto_alt avg `-0.0161` n `230`; crypto_major avg `-0.1654` n `8`; equity avg `-0.4548` n `102`; fx avg `-0.05` n `6`; index avg `-0.0996` n `25`; metal avg `0.044` n `20`; unknown avg `-0.0561` n `758`
- 24h: commodity avg `-0.7305` n `12`; crypto_alt avg `-3.6777` n `230`; crypto_major avg `-3.5407` n `8`; equity avg `-4.1823` n `102`; fx avg `-0.1715` n `6`; index avg `-0.8729` n `25`; metal avg `-0.3572` n `20`; unknown avg `1158.5561` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
