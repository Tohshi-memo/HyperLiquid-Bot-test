# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T15:07:25.103465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0362` n `12`; crypto_alt avg `0.2454` n `229`; crypto_major avg `0.1106` n `8`; equity avg `0.0004` n `88`; fx avg `0.0152` n `6`; index avg `-0.0002` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.0693` n `765`
- 1h: commodity avg `0.0527` n `12`; crypto_alt avg `0.1774` n `229`; crypto_major avg `0.2936` n `8`; equity avg `0.0088` n `88`; fx avg `0.0397` n `6`; index avg `0.0114` n `25`; metal avg `0.01` n `20`; unknown avg `-0.0302` n `765`
- 4h: commodity avg `0.013` n `12`; crypto_alt avg `0.8093` n `229`; crypto_major avg `0.7463` n `8`; equity avg `-0.0298` n `88`; fx avg `0.036` n `6`; index avg `0.0027` n `25`; metal avg `0.0165` n `20`; unknown avg `-0.0862` n `759`
- 24h: commodity avg `0.0956` n `12`; crypto_alt avg `0.6531` n `229`; crypto_major avg `1.1645` n `8`; equity avg `0.1596` n `88`; fx avg `-0.0339` n `6`; index avg `-0.0254` n `25`; metal avg `-0.0431` n `20`; unknown avg `2.0761` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
