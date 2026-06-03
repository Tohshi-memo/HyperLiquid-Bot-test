# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T08:52:23.126207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.7749` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0465` n `12`; crypto_alt avg `-0.0315` n `228`; crypto_major avg `0.0514` n `8`; equity avg `0.0533` n `72`; fx avg `-0.016` n `6`; index avg `-0.0345` n `23`; metal avg `-0.1202` n `18`; unknown avg `-0.0051` n `420`
- 1h: commodity avg `0.2753` n `12`; crypto_alt avg `-0.1414` n `228`; crypto_major avg `-0.3258` n `8`; equity avg `-0.1738` n `72`; fx avg `-0.0215` n `6`; index avg `-0.0748` n `23`; metal avg `-0.1214` n `18`; unknown avg `0.9143` n `420`
- 4h: commodity avg `0.6352` n `12`; crypto_alt avg `2.0462` n `228`; crypto_major avg `1.1585` n `8`; equity avg `0.0145` n `72`; fx avg `0.0356` n `6`; index avg `-0.0625` n `23`; metal avg `-0.6164` n `18`; unknown avg `0.6538` n `410`
- 24h: commodity avg `1.9272` n `12`; crypto_alt avg `-0.9561` n `228`; crypto_major avg `-3.2603` n `8`; equity avg `0.5589` n `72`; fx avg `0.0189` n `6`; index avg `0.7901` n `23`; metal avg `-1.7602` n `18`; unknown avg `1.59` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0476`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
