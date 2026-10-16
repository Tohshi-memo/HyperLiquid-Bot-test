# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T23:22:30.994492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `-0.0145` n `236`; crypto_major avg `-0.0036` n `8`; equity avg `0.0016` n `151`; fx avg `0.0007` n `6`; index avg `-0.02` n `26`; metal avg `0.0046` n `20`; unknown avg `0.1263` n `1193`
- 1h: commodity avg `0.031` n `13`; crypto_alt avg `0.0279` n `236`; crypto_major avg `-0.0271` n `8`; equity avg `-0.1734` n `151`; fx avg `0.0053` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.9479` n `1191`
- 4h: commodity avg `0.0078` n `13`; crypto_alt avg `0.6465` n `236`; crypto_major avg `0.6175` n `8`; equity avg `-0.5802` n `151`; fx avg `0.0095` n `6`; index avg `-0.0743` n `26`; metal avg `0.0252` n `20`; unknown avg `0.4631` n `1107`
- 24h: commodity avg `0.4538` n `13`; crypto_alt avg `-0.9454` n `236`; crypto_major avg `-0.7435` n `8`; equity avg `-4.0367` n `151`; fx avg `0.0384` n `6`; index avg `-0.6366` n `26`; metal avg `-0.0529` n `20`; unknown avg `40.6951` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1659`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1173`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0876`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0704`, n `666`, weak_sample_signal
