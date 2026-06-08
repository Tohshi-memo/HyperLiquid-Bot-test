# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T20:07:25.909629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.069` n `228`; crypto_major avg `0.0767` n `8`; equity avg `0.1325` n `74`; fx avg `0.0125` n `6`; index avg `0.0273` n `23`; metal avg `0.0042` n `18`; unknown avg `0.0136` n `517`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `-0.3871` n `228`; crypto_major avg `-0.2225` n `8`; equity avg `-0.1164` n `74`; fx avg `0.0093` n `6`; index avg `-0.2119` n `23`; metal avg `-0.077` n `18`; unknown avg `-0.1241` n `517`
- 4h: commodity avg `-0.0553` n `12`; crypto_alt avg `-0.2055` n `228`; crypto_major avg `-0.2982` n `8`; equity avg `-0.4476` n `74`; fx avg `-0.0177` n `6`; index avg `-0.4435` n `23`; metal avg `-0.2919` n `18`; unknown avg `-0.1364` n `517`
- 24h: commodity avg `-1.0278` n `12`; crypto_alt avg `3.7376` n `228`; crypto_major avg `4.1841` n `8`; equity avg `2.701` n `74`; fx avg `-0.3054` n `6`; index avg `0.9896` n `23`; metal avg `0.1354` n `18`; unknown avg `-1.4806` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
