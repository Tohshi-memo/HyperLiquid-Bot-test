# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T07:24:55.548605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `0.0061` n `231`; crypto_major avg `-0.0306` n `8`; equity avg `-0.0731` n `122`; fx avg `0.0059` n `6`; index avg `-0.009` n `25`; metal avg `0.0198` n `20`; unknown avg `-0.0173` n `797`
- 1h: commodity avg `-0.0795` n `12`; crypto_alt avg `0.0606` n `231`; crypto_major avg `0.2156` n `8`; equity avg `0.0184` n `122`; fx avg `0.0042` n `6`; index avg `0.0058` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.0858` n `797`
- 4h: commodity avg `0.0758` n `12`; crypto_alt avg `-0.0953` n `231`; crypto_major avg `0.0677` n `8`; equity avg `-0.2247` n `122`; fx avg `-0.0354` n `6`; index avg `-0.0207` n `25`; metal avg `-0.1217` n `20`; unknown avg `0.107` n `781`
- 24h: commodity avg `-0.6125` n `12`; crypto_alt avg `-2.4072` n `231`; crypto_major avg `-2.4636` n `8`; equity avg `0.5333` n `122`; fx avg `-0.0296` n `6`; index avg `0.0861` n `25`; metal avg `0.0985` n `20`; unknown avg `0.8091` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
