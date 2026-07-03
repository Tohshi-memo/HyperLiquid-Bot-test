# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T06:52:25.222025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `0.0208` n `229`; crypto_major avg `-0.0265` n `8`; equity avg `0.0216` n `88`; fx avg `0.0073` n `6`; index avg `-0.0247` n `25`; metal avg `0.0132` n `20`; unknown avg `-0.0482` n `763`
- 1h: commodity avg `-0.0197` n `12`; crypto_alt avg `0.1344` n `229`; crypto_major avg `-0.0587` n `8`; equity avg `0.1334` n `88`; fx avg `-0.156` n `6`; index avg `0.0459` n `25`; metal avg `0.009` n `20`; unknown avg `-0.213` n `743`
- 4h: commodity avg `0.1177` n `12`; crypto_alt avg `0.3071` n `229`; crypto_major avg `0.535` n `8`; equity avg `0.5334` n `88`; fx avg `-0.1066` n `6`; index avg `0.1743` n `25`; metal avg `-0.0765` n `20`; unknown avg `-0.3973` n `743`
- 24h: commodity avg `0.5282` n `12`; crypto_alt avg `2.5159` n `228`; crypto_major avg `3.6247` n `8`; equity avg `0.6113` n `88`; fx avg `-0.1329` n `6`; index avg `0.2299` n `25`; metal avg `1.2181` n `20`; unknown avg `5.9113` n `741`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
