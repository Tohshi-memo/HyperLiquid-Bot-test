# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T21:37:20.655479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0431` n `12`; crypto_alt avg `0.0482` n `228`; crypto_major avg `0.0854` n `8`; equity avg `-0.0084` n `66`; fx avg `-0.0095` n `6`; index avg `0.0137` n `23`; metal avg `-0.0073` n `18`; unknown avg `-0.0347` n `384`
- 1h: commodity avg `0.1384` n `12`; crypto_alt avg `0.0875` n `228`; crypto_major avg `0.1674` n `8`; equity avg `0.1025` n `66`; fx avg `-0.0052` n `6`; index avg `-0.0339` n `23`; metal avg `-0.0496` n `18`; unknown avg `-0.0133` n `384`
- 4h: commodity avg `0.5916` n `12`; crypto_alt avg `-0.1997` n `228`; crypto_major avg `-0.1584` n `8`; equity avg `0.0127` n `66`; fx avg `-0.0463` n `6`; index avg `0.0739` n `23`; metal avg `-0.0494` n `18`; unknown avg `-0.0925` n `384`
- 24h: commodity avg `-2.3` n `12`; crypto_alt avg `2.5146` n `228`; crypto_major avg `1.9366` n `8`; equity avg `1.606` n `66`; fx avg `-0.0844` n `6`; index avg `1.1173` n `23`; metal avg `1.4938` n `18`; unknown avg `0.9573` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0441`, n `668`, weak_sample_signal
