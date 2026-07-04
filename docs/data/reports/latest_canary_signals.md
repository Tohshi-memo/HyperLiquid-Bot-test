# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T15:22:25.733471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0458` n `12`; crypto_alt avg `0.3216` n `229`; crypto_major avg `0.297` n `8`; equity avg `0.0512` n `88`; fx avg `-0.0092` n `6`; index avg `0.0004` n `25`; metal avg `-0.0006` n `20`; unknown avg `0.1472` n `765`
- 1h: commodity avg `0.0238` n `12`; crypto_alt avg `0.5973` n `229`; crypto_major avg `0.5457` n `8`; equity avg `0.0677` n `88`; fx avg `0.0208` n `6`; index avg `-0.0006` n `25`; metal avg `0.0141` n `20`; unknown avg `0.1274` n `765`
- 4h: commodity avg `-0.0487` n `12`; crypto_alt avg `1.0947` n `229`; crypto_major avg `1.0764` n `8`; equity avg `0.0145` n `88`; fx avg `0.0324` n `6`; index avg `0.0027` n `25`; metal avg `0.0096` n `20`; unknown avg `0.06` n `759`
- 24h: commodity avg `0.0843` n `12`; crypto_alt avg `1.2067` n `229`; crypto_major avg `1.8005` n `8`; equity avg `0.2916` n `88`; fx avg `-0.0324` n `6`; index avg `-0.0346` n `25`; metal avg `-0.0103` n `20`; unknown avg `2.0858` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
