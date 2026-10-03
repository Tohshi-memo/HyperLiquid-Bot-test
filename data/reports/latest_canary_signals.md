# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T02:37:26.624314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.0925` n `235`; crypto_major avg `-0.0468` n `8`; equity avg `0.0036` n `143`; fx avg `-0.0009` n `6`; index avg `0.0003` n `26`; metal avg `0.0035` n `20`; unknown avg `0.4964` n `984`
- 1h: commodity avg `-0.0112` n `13`; crypto_alt avg `0.037` n `235`; crypto_major avg `-0.1196` n `8`; equity avg `0.0525` n `143`; fx avg `0.0018` n `6`; index avg `0.0155` n `26`; metal avg `0.0223` n `20`; unknown avg `0.0971` n `982`
- 4h: commodity avg `-0.2398` n `13`; crypto_alt avg `1.0745` n `235`; crypto_major avg `0.5506` n `8`; equity avg `0.0867` n `143`; fx avg `0.0174` n `6`; index avg `0.045` n `26`; metal avg `0.0024` n `20`; unknown avg `0.0962` n `976`
- 24h: commodity avg `0.0378` n `13`; crypto_alt avg `-0.4833` n `235`; crypto_major avg `-0.3743` n `8`; equity avg `0.7107` n `142`; fx avg `-0.1117` n `6`; index avg `0.2833` n `26`; metal avg `-0.0995` n `20`; unknown avg `-0.7106` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
