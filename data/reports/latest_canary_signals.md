# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T16:37:25.524745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0643` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.3612` n `232`; crypto_major avg `0.2357` n `8`; equity avg `0.0408` n `134`; fx avg `-0.0025` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.0204` n `790`
- 1h: commodity avg `-0.1104` n `12`; crypto_alt avg `0.5481` n `232`; crypto_major avg `0.4013` n `8`; equity avg `0.0413` n `134`; fx avg `-0.0084` n `6`; index avg `0.0133` n `26`; metal avg `0.0211` n `20`; unknown avg `0.4919` n `788`
- 4h: commodity avg `-0.0533` n `12`; crypto_alt avg `-0.67` n `232`; crypto_major avg `-1.0198` n `8`; equity avg `0.0059` n `134`; fx avg `-0.0248` n `6`; index avg `0.0445` n `26`; metal avg `0.1492` n `20`; unknown avg `-0.6193` n `788`
- 24h: commodity avg `0.1135` n `12`; crypto_alt avg `0.044` n `232`; crypto_major avg `-0.9889` n `8`; equity avg `0.4122` n `134`; fx avg `-0.1126` n `6`; index avg `0.0609` n `26`; metal avg `0.0299` n `20`; unknown avg `148.025` n `681`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
