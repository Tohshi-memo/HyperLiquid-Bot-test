# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T08:07:21.004233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `12`; crypto_alt avg `-0.0777` n `228`; crypto_major avg `-0.2077` n `8`; equity avg `0.0996` n `74`; fx avg `-0.0226` n `6`; index avg `-0.0554` n `23`; metal avg `-0.0597` n `18`; unknown avg `0.028` n `517`
- 1h: commodity avg `-0.1422` n `12`; crypto_alt avg `0.6396` n `228`; crypto_major avg `0.3656` n `8`; equity avg `0.6978` n `74`; fx avg `0.0043` n `6`; index avg `0.1994` n `23`; metal avg `0.1025` n `18`; unknown avg `0.0962` n `517`
- 4h: commodity avg `0.1559` n `12`; crypto_alt avg `0.4296` n `228`; crypto_major avg `0.3518` n `8`; equity avg `-0.006` n `74`; fx avg `-0.2289` n `6`; index avg `-0.0227` n `23`; metal avg `-0.4906` n `18`; unknown avg `0.002` n `507`
- 24h: commodity avg `0.9529` n `12`; crypto_alt avg `0.6481` n `228`; crypto_major avg `1.9566` n `8`; equity avg `0.9246` n `74`; fx avg `-0.3315` n `6`; index avg `0.189` n `23`; metal avg `-0.7976` n `18`; unknown avg `-5.2423` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
