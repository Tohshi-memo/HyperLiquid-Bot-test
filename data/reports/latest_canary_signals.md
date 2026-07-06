# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T18:52:26.184661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5187` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.0783` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8001` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0167` n `12`; crypto_alt avg `-0.0192` n `229`; crypto_major avg `0.0752` n `8`; equity avg `-0.0416` n `91`; fx avg `-0.0087` n `6`; index avg `0.0023` n `25`; metal avg `-0.0474` n `20`; unknown avg `-0.0003` n `763`
- 1h: commodity avg `0.0568` n `12`; crypto_alt avg `0.1413` n `229`; crypto_major avg `0.2578` n `8`; equity avg `-0.0684` n `91`; fx avg `-0.0014` n `6`; index avg `0.0322` n `25`; metal avg `0.0558` n `20`; unknown avg `-0.0713` n `763`
- 4h: commodity avg `0.0072` n `12`; crypto_alt avg `1.8478` n `229`; crypto_major avg `2.0855` n `8`; equity avg `-0.4332` n `90`; fx avg `0.025` n `6`; index avg `-0.0279` n `25`; metal avg `0.2854` n `20`; unknown avg `2.537` n `763`
- 24h: commodity avg `0.0248` n `12`; crypto_alt avg `0.8963` n `229`; crypto_major avg `0.6362` n `8`; equity avg `-0.7359` n `90`; fx avg `0.2021` n `6`; index avg `0.0165` n `25`; metal avg `-0.1615` n `20`; unknown avg `0.8152` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
