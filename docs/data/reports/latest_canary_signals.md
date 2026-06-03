# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T20:07:32.616149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0423` n `12`; crypto_alt avg `-0.0844` n `228`; crypto_major avg `-0.0251` n `8`; equity avg `-0.2585` n `73`; fx avg `0.0035` n `6`; index avg `-0.1161` n `23`; metal avg `-0.1652` n `18`; unknown avg `0.0` n `419`
- 1h: commodity avg `0.0367` n `12`; crypto_alt avg `-0.9311` n `228`; crypto_major avg `-0.9214` n `8`; equity avg `-0.2357` n `73`; fx avg `0.0162` n `6`; index avg `-0.1077` n `23`; metal avg `-0.2534` n `18`; unknown avg `-0.1395` n `419`
- 4h: commodity avg `0.0904` n `12`; crypto_alt avg `-0.4859` n `228`; crypto_major avg `-0.7743` n `8`; equity avg `-0.2892` n `73`; fx avg `0.0206` n `6`; index avg `-0.0755` n `23`; metal avg `-0.3724` n `18`; unknown avg `-0.1948` n `419`
- 24h: commodity avg `0.8813` n `12`; crypto_alt avg `0.3947` n `228`; crypto_major avg `-2.6457` n `8`; equity avg `-2.2751` n `72`; fx avg `0.0478` n `6`; index avg `-0.5092` n `23`; metal avg `-2.2154` n `18`; unknown avg `0.0729` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.043`, n `668`, weak_sample_signal
