# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T07:07:25.675628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.19` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.6101` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.097` n `12`; crypto_alt avg `-0.134` n `228`; crypto_major avg `0.0549` n `8`; equity avg `-0.0842` n `72`; fx avg `-0.0014` n `6`; index avg `0.0322` n `23`; metal avg `0.0802` n `18`; unknown avg `-0.0277` n `420`
- 1h: commodity avg `0.2068` n `12`; crypto_alt avg `0.1135` n `228`; crypto_major avg `0.0085` n `8`; equity avg `-0.1011` n `72`; fx avg `0.0331` n `6`; index avg `0.0184` n `23`; metal avg `-0.084` n `18`; unknown avg `-0.1612` n `420`
- 4h: commodity avg `0.4482` n `12`; crypto_alt avg `1.7937` n `228`; crypto_major avg `1.0314` n `8`; equity avg `0.357` n `72`; fx avg `0.0559` n `6`; index avg `0.0244` n `23`; metal avg `-0.5787` n `18`; unknown avg `0.369` n `410`
- 24h: commodity avg `1.2216` n `12`; crypto_alt avg `-0.9313` n `228`; crypto_major avg `-3.2012` n `8`; equity avg `0.9063` n `72`; fx avg `0.0348` n `6`; index avg `1.0729` n `23`; metal avg `-1.6437` n `18`; unknown avg `-0.563` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
