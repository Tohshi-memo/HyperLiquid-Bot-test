# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T14:07:29.921441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0253` n `12`; crypto_alt avg `-0.0202` n `228`; crypto_major avg `-0.0178` n `8`; equity avg `0.2763` n `88`; fx avg `-0.0217` n `6`; index avg `0.0344` n `23`; metal avg `0.0693` n `20`; unknown avg `-0.0844` n `765`
- 1h: commodity avg `-0.1224` n `12`; crypto_alt avg `0.8662` n `228`; crypto_major avg `1.091` n `8`; equity avg `0.965` n `88`; fx avg `-0.0067` n `6`; index avg `0.0205` n `23`; metal avg `0.9314` n `20`; unknown avg `0.3909` n `765`
- 4h: commodity avg `-0.0976` n `12`; crypto_alt avg `0.6824` n `228`; crypto_major avg `0.6251` n `8`; equity avg `-0.0378` n `88`; fx avg `-0.0523` n `6`; index avg `-0.0524` n `23`; metal avg `1.176` n `20`; unknown avg `-0.0491` n `765`
- 24h: commodity avg `-0.6531` n `12`; crypto_alt avg `1.0168` n `228`; crypto_major avg `0.5432` n `8`; equity avg `0.371` n `88`; fx avg `0.0779` n `6`; index avg `-0.2134` n `23`; metal avg `0.5582` n `20`; unknown avg `-0.0308` n `743`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
