# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T15:37:25.028136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2828` n `12`; crypto_alt avg `-0.2799` n `228`; crypto_major avg `-0.0535` n `8`; equity avg `-0.1465` n `73`; fx avg `0.0309` n `6`; index avg `-0.0741` n `23`; metal avg `-0.0512` n `18`; unknown avg `-0.3438` n `419`
- 1h: commodity avg `0.341` n `12`; crypto_alt avg `-0.3081` n `228`; crypto_major avg `-0.429` n `8`; equity avg `-0.5041` n `73`; fx avg `0.0499` n `6`; index avg `-0.1914` n `23`; metal avg `-0.2755` n `18`; unknown avg `-0.3496` n `419`
- 4h: commodity avg `-0.2284` n `12`; crypto_alt avg `-0.1303` n `228`; crypto_major avg `-1.076` n `8`; equity avg `-2.0765` n `73`; fx avg `-0.0042` n `6`; index avg `-0.6204` n `23`; metal avg `-1.0768` n `18`; unknown avg `-0.2651` n `419`
- 24h: commodity avg `1.3965` n `12`; crypto_alt avg `3.0561` n `228`; crypto_major avg `-1.2342` n `8`; equity avg `-1.5468` n `72`; fx avg `0.0409` n `6`; index avg `-0.237` n `23`; metal avg `-2.219` n `18`; unknown avg `0.8403` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
