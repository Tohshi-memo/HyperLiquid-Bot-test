# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T11:52:32.226762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2136` n `12`; crypto_alt avg `-0.3713` n `228`; crypto_major avg `-0.3399` n `8`; equity avg `-0.1345` n `74`; fx avg `-0.0216` n `6`; index avg `-0.0609` n `23`; metal avg `0.0691` n `18`; unknown avg `-0.0379` n `517`
- 1h: commodity avg `-0.9047` n `12`; crypto_alt avg `0.7632` n `228`; crypto_major avg `0.8438` n `8`; equity avg `0.8372` n `74`; fx avg `-0.0083` n `6`; index avg `0.3814` n `23`; metal avg `0.8436` n `18`; unknown avg `0.1533` n `517`
- 4h: commodity avg `-1.1933` n `12`; crypto_alt avg `0.9196` n `228`; crypto_major avg `0.3824` n `8`; equity avg `1.0682` n `74`; fx avg `-0.0024` n `6`; index avg `0.5239` n `23`; metal avg `0.9028` n `18`; unknown avg `-0.0681` n `517`
- 24h: commodity avg `-0.3925` n `12`; crypto_alt avg `1.2498` n `228`; crypto_major avg `2.2828` n `8`; equity avg `1.8455` n `74`; fx avg `-0.2765` n `6`; index avg `0.8378` n `23`; metal avg `0.1616` n `18`; unknown avg `-2.33` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
