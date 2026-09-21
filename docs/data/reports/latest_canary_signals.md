# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T03:07:29.081873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0401` n `12`; crypto_alt avg `0.371` n `234`; crypto_major avg `0.0929` n `8`; equity avg `0.0363` n `140`; fx avg `-0.0204` n `6`; index avg `0.0091` n `26`; metal avg `-0.0268` n `20`; unknown avg `0.1614` n `942`
- 1h: commodity avg `-0.0032` n `12`; crypto_alt avg `0.9006` n `234`; crypto_major avg `0.3434` n `8`; equity avg `0.0524` n `140`; fx avg `-0.0539` n `6`; index avg `0.0238` n `26`; metal avg `-0.0886` n `20`; unknown avg `-0.3252` n `942`
- 4h: commodity avg `-0.3475` n `12`; crypto_alt avg `0.6094` n `234`; crypto_major avg `0.5652` n `8`; equity avg `0.4187` n `140`; fx avg `-0.098` n `6`; index avg `0.0694` n `26`; metal avg `-0.0292` n `20`; unknown avg `36.5826` n `935`
- 24h: commodity avg `-0.6459` n `12`; crypto_alt avg `2.8173` n `234`; crypto_major avg `2.4205` n `8`; equity avg `1.0758` n `140`; fx avg `-0.0504` n `6`; index avg `0.1978` n `26`; metal avg `0.0287` n `20`; unknown avg `3.7051` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
