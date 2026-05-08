# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T12:52:20.149961+00:00`
- Correlation status: `ready`
- Asset price records: `647`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.048` n `12`; crypto_alt avg `-0.0268` n `228`; crypto_major avg `-0.2228` n `8`; equity avg `-0.0021` n `65`; fx avg `-0.0107` n `5`; index avg `0.0453` n `23`; metal avg `0.0515` n `18`; unknown avg `-0.1382` n `375`
- 1h: commodity avg `0.0677` n `12`; crypto_alt avg `-0.2321` n `228`; crypto_major avg `-0.2619` n `8`; equity avg `0.1704` n `65`; fx avg `-0.0322` n `5`; index avg `0.2117` n `23`; metal avg `0.3296` n `18`; unknown avg `-0.0027` n `375`
- 4h: commodity avg `0.1171` n `12`; crypto_alt avg `0.0987` n `228`; crypto_major avg `-0.0266` n `8`; equity avg `0.2613` n `65`; fx avg `-0.0196` n `5`; index avg `0.2842` n `23`; metal avg `0.3513` n `18`; unknown avg `-0.069` n `375`
- 24h: commodity avg `2.3498` n `12`; crypto_alt avg `0.3746` n `228`; crypto_major avg `-1.7056` n `8`; equity avg `-0.2453` n `65`; fx avg `0.2473` n `5`; index avg `-0.0893` n `23`; metal avg `-0.6903` n `18`; unknown avg `-0.2846` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1312`, n `639`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.13`, n `639`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `643`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `643`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0914`, n `643`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `643`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0893`, n `639`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0863`, n `639`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `643`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `643`, weak_sample_signal
