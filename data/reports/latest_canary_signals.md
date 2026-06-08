# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T04:07:30.128872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.066` n `12`; crypto_alt avg `-0.2951` n `228`; crypto_major avg `-0.3901` n `8`; equity avg `-0.1107` n `74`; fx avg `-0.0056` n `6`; index avg `-0.089` n `23`; metal avg `0.1016` n `18`; unknown avg `-0.0005` n `517`
- 1h: commodity avg `-0.0197` n `12`; crypto_alt avg `-0.1744` n `228`; crypto_major avg `-0.4932` n `8`; equity avg `-0.2655` n `74`; fx avg `-0.0023` n `6`; index avg `-0.1331` n `23`; metal avg `0.2259` n `18`; unknown avg `2.266` n `517`
- 4h: commodity avg `0.2772` n `12`; crypto_alt avg `-0.425` n `228`; crypto_major avg `-0.2121` n `8`; equity avg `0.4759` n `74`; fx avg `-0.0314` n `6`; index avg `0.2237` n `23`; metal avg `-0.3978` n `18`; unknown avg `-0.5323` n `517`
- 24h: commodity avg `0.4107` n `12`; crypto_alt avg `1.0418` n `228`; crypto_major avg `3.1013` n `8`; equity avg `1.5567` n `74`; fx avg `-0.102` n `6`; index avg `0.2191` n `23`; metal avg `-0.1378` n `18`; unknown avg `-5.4585` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
