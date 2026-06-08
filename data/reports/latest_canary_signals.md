# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T23:22:21.780274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.3879` n `228`; crypto_major avg `-0.3919` n `8`; equity avg `0.0598` n `74`; fx avg `-0.0022` n `6`; index avg `0.0624` n `23`; metal avg `-0.0089` n `18`; unknown avg `0.0596` n `517`
- 1h: commodity avg `-0.0275` n `12`; crypto_alt avg `-0.4945` n `228`; crypto_major avg `-0.1181` n `8`; equity avg `0.1625` n `74`; fx avg `-0.0073` n `6`; index avg `0.0869` n `23`; metal avg `0.0353` n `18`; unknown avg `-0.7007` n `517`
- 4h: commodity avg `0.061` n `12`; crypto_alt avg `-1.2556` n `228`; crypto_major avg `-0.6147` n `8`; equity avg `0.1713` n `74`; fx avg `-0.0036` n `6`; index avg `0.2004` n `23`; metal avg `0.0819` n `18`; unknown avg `-0.935` n `517`
- 24h: commodity avg `-0.5862` n `12`; crypto_alt avg `0.9875` n `228`; crypto_major avg `1.7369` n `8`; equity avg `2.2683` n `74`; fx avg `-0.2751` n `6`; index avg `1.0917` n `23`; metal avg `0.0543` n `18`; unknown avg `-2.919` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
