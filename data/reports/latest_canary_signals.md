# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T16:22:36.441468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0342` n `12`; crypto_alt avg `-0.4119` n `234`; crypto_major avg `-0.5262` n `8`; equity avg `-0.0848` n `140`; fx avg `-0.0015` n `6`; index avg `-0.007` n `26`; metal avg `-0.0046` n `20`; unknown avg `0.0997` n `942`
- 1h: commodity avg `0.0582` n `12`; crypto_alt avg `-0.3371` n `234`; crypto_major avg `-0.6571` n `8`; equity avg `-0.0504` n `140`; fx avg `0.0124` n `6`; index avg `-0.0198` n `26`; metal avg `-0.1008` n `20`; unknown avg `0.2847` n `920`
- 4h: commodity avg `0.4159` n `12`; crypto_alt avg `0.4537` n `234`; crypto_major avg `-0.0797` n `8`; equity avg `0.6353` n `140`; fx avg `-0.036` n `6`; index avg `0.088` n `26`; metal avg `-0.0855` n `20`; unknown avg `2.6387` n `886`
- 24h: commodity avg `0.305` n `12`; crypto_alt avg `0.2116` n `234`; crypto_major avg `0.4898` n `8`; equity avg `0.5701` n `140`; fx avg `-0.2671` n `6`; index avg `0.0872` n `26`; metal avg `-0.1343` n `20`; unknown avg `3978.7048` n `834`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
