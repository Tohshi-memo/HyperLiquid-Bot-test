# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T21:52:29.642023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0347` n `12`; crypto_alt avg `0.0775` n `230`; crypto_major avg `0.1541` n `8`; equity avg `0.0263` n `92`; fx avg `-0.0083` n `6`; index avg `0.0011` n `25`; metal avg `0.0114` n `20`; unknown avg `0.0939` n `766`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.5287` n `230`; crypto_major avg `-0.3092` n `8`; equity avg `0.025` n `92`; fx avg `0.0066` n `6`; index avg `0.024` n `25`; metal avg `0.0205` n `20`; unknown avg `0.0459` n `766`
- 4h: commodity avg `0.1844` n `12`; crypto_alt avg `-0.7563` n `230`; crypto_major avg `-0.3236` n `8`; equity avg `0.0774` n `92`; fx avg `-0.0087` n `6`; index avg `-0.0525` n `25`; metal avg `0.0767` n `20`; unknown avg `-0.3269` n `766`
- 24h: commodity avg `0.6845` n `12`; crypto_alt avg `-2.7762` n `230`; crypto_major avg `-3.1307` n `8`; equity avg `-3.2891` n `92`; fx avg `-0.0472` n `6`; index avg `-0.6675` n `25`; metal avg `-0.5019` n `20`; unknown avg `-0.4165` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
