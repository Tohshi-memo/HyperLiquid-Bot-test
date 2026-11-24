# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T21:52:29.126210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `13`; crypto_alt avg `-0.0485` n `239`; crypto_major avg `0.0095` n `8`; equity avg `-0.0146` n `168`; fx avg `0.0018` n `6`; index avg `-0.0067` n `27`; metal avg `0.0094` n `20`; unknown avg `26.2197` n `1265`
- 1h: commodity avg `0.0365` n `13`; crypto_alt avg `-0.3738` n `239`; crypto_major avg `-0.009` n `8`; equity avg `-0.3047` n `168`; fx avg `-0.0118` n `6`; index avg `-0.042` n `27`; metal avg `0.0011` n `20`; unknown avg `38.9051` n `1241`
- 4h: commodity avg `0.0745` n `13`; crypto_alt avg `-0.7394` n `239`; crypto_major avg `-0.0847` n `8`; equity avg `-0.0532` n `168`; fx avg `-0.0514` n `6`; index avg `-0.019` n `27`; metal avg `0.009` n `20`; unknown avg `398.9481` n `1211`
- 24h: commodity avg `0.615` n `13`; crypto_alt avg `-2.989` n `239`; crypto_major avg `-2.5547` n `8`; equity avg `-4.0851` n `167`; fx avg `0.2295` n `6`; index avg `-0.2778` n `27`; metal avg `-1.048` n `20`; unknown avg `424.4358` n `1111`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
