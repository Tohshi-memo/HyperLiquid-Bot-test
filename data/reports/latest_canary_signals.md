# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T06:22:31.846499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.1145` n `228`; crypto_major avg `0.0117` n `8`; equity avg `0.0948` n `79`; fx avg `0.0217` n `6`; index avg `0.0095` n `23`; metal avg `0.0278` n `18`; unknown avg `-0.0816` n `701`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.1557` n `228`; crypto_major avg `-0.1489` n `8`; equity avg `0.0548` n `79`; fx avg `-0.0087` n `6`; index avg `0.0046` n `23`; metal avg `0.296` n `18`; unknown avg `0.6425` n `669`
- 4h: commodity avg `-0.0862` n `12`; crypto_alt avg `-0.5311` n `228`; crypto_major avg `-0.7069` n `8`; equity avg `-0.1019` n `79`; fx avg `-0.0353` n `6`; index avg `-0.0144` n `23`; metal avg `0.2802` n `18`; unknown avg `0.0444` n `669`
- 24h: commodity avg `-0.3803` n `12`; crypto_alt avg `0.0854` n `228`; crypto_major avg `-0.4948` n `8`; equity avg `-0.465` n `79`; fx avg `-0.0122` n `6`; index avg `-0.0132` n `23`; metal avg `0.4803` n `18`; unknown avg `-0.3371` n `643`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
