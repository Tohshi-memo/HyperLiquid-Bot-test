# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T22:37:27.706936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `-0.013` n `233`; crypto_major avg `0.1659` n `8`; equity avg `0.0222` n `136`; fx avg `0.0175` n `6`; index avg `0.026` n `27`; metal avg `0.0503` n `20`; unknown avg `0.6293` n `840`
- 1h: commodity avg `0.3087` n `12`; crypto_alt avg `-1.7362` n `233`; crypto_major avg `-1.0513` n `8`; equity avg `-0.3858` n `136`; fx avg `0.0207` n `6`; index avg `-0.0775` n `27`; metal avg `-0.0862` n `20`; unknown avg `5.122` n `838`
- 4h: commodity avg `0.4002` n `12`; crypto_alt avg `-1.8335` n `233`; crypto_major avg `-0.9867` n `8`; equity avg `-0.3611` n `136`; fx avg `0.0515` n `6`; index avg `-0.0627` n `27`; metal avg `-0.0901` n `20`; unknown avg `5.4782` n `794`
- 24h: commodity avg `0.6441` n `12`; crypto_alt avg `-1.3611` n `233`; crypto_major avg `-1.4023` n `8`; equity avg `-1.4022` n `136`; fx avg `0.0684` n `6`; index avg `-0.2933` n `26`; metal avg `-0.1402` n `20`; unknown avg `2.2674` n `716`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
