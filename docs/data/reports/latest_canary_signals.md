# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T21:07:29.599344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `0.0261` n `230`; crypto_major avg `0.0028` n `8`; equity avg `0.067` n `100`; fx avg `-0.0138` n `6`; index avg `0.0101` n `25`; metal avg `0.038` n `20`; unknown avg `44.3936` n `772`
- 1h: commodity avg `0.1393` n `12`; crypto_alt avg `0.0878` n `230`; crypto_major avg `0.0644` n `8`; equity avg `0.2315` n `100`; fx avg `-0.0106` n `6`; index avg `0.0082` n `25`; metal avg `0.0435` n `20`; unknown avg `44.2501` n `772`
- 4h: commodity avg `-0.0604` n `12`; crypto_alt avg `-0.1055` n `230`; crypto_major avg `0.0335` n `8`; equity avg `0.2427` n `100`; fx avg `0.0021` n `6`; index avg `0.1104` n `25`; metal avg `-0.0136` n `20`; unknown avg `43.9854` n `772`
- 24h: commodity avg `0.9737` n `12`; crypto_alt avg `-1.4336` n `230`; crypto_major avg `-1.8618` n `8`; equity avg `-1.2759` n `99`; fx avg `-0.0861` n `6`; index avg `-0.2815` n `25`; metal avg `-0.7309` n `20`; unknown avg `45.8268` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
