# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T21:37:28.607791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0332` n `231`; crypto_major avg `-0.0359` n `8`; equity avg `0.017` n `128`; fx avg `-0.0014` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.0015` n `792`
- 1h: commodity avg `0.0147` n `12`; crypto_alt avg `-0.0593` n `231`; crypto_major avg `-0.0144` n `8`; equity avg `0.0051` n `128`; fx avg `-0.0067` n `6`; index avg `0.0001` n `26`; metal avg `0.004` n `20`; unknown avg `3.7937` n `792`
- 4h: commodity avg `-0.0092` n `12`; crypto_alt avg `0.1845` n `231`; crypto_major avg `0.2351` n `8`; equity avg `0.2062` n `128`; fx avg `-0.0201` n `6`; index avg `0.0334` n `26`; metal avg `0.0201` n `20`; unknown avg `0.2119` n `792`
- 24h: commodity avg `-0.046` n `12`; crypto_alt avg `0.6523` n `231`; crypto_major avg `0.9504` n `8`; equity avg `0.4376` n `128`; fx avg `-0.0242` n `6`; index avg `0.0862` n `26`; metal avg `0.1415` n `20`; unknown avg `0.0641` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
