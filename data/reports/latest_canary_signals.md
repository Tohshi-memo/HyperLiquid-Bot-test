# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T14:22:30.333305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.022` n `12`; crypto_alt avg `0.1321` n `233`; crypto_major avg `0.0947` n `8`; equity avg `0.0127` n `136`; fx avg `-0.0025` n `6`; index avg `0.0005` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.0553` n `840`
- 1h: commodity avg `-0.0235` n `12`; crypto_alt avg `0.1863` n `233`; crypto_major avg `0.1655` n `8`; equity avg `0.0268` n `136`; fx avg `-0.0081` n `6`; index avg `0.0005` n `26`; metal avg `0.0076` n `20`; unknown avg `-0.163` n `836`
- 4h: commodity avg `-0.0353` n `12`; crypto_alt avg `0.1067` n `233`; crypto_major avg `0.1728` n `8`; equity avg `0.0183` n `136`; fx avg `-0.0019` n `6`; index avg `-0.0019` n `26`; metal avg `0.0339` n `20`; unknown avg `0.3081` n `824`
- 24h: commodity avg `-0.2643` n `12`; crypto_alt avg `-0.7168` n `233`; crypto_major avg `-1.5959` n `8`; equity avg `-0.528` n `136`; fx avg `-0.0077` n `6`; index avg `-0.0123` n `26`; metal avg `-0.2254` n `20`; unknown avg `9.1373` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
