# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T05:52:31.543251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `-0.1585` n `228`; crypto_major avg `-0.1415` n `8`; equity avg `0.0648` n `74`; fx avg `-0.0048` n `6`; index avg `0.0288` n `23`; metal avg `0.1189` n `18`; unknown avg `-0.505` n `517`
- 1h: commodity avg `-0.0916` n `12`; crypto_alt avg `0.3561` n `228`; crypto_major avg `0.2496` n `8`; equity avg `0.2841` n `74`; fx avg `-0.0606` n `6`; index avg `0.1719` n `23`; metal avg `0.4608` n `18`; unknown avg `-0.563` n `517`
- 4h: commodity avg `-0.2241` n `12`; crypto_alt avg `0.9818` n `228`; crypto_major avg `1.046` n `8`; equity avg `1.1157` n `74`; fx avg `-0.0369` n `6`; index avg `0.5161` n `23`; metal avg `0.3333` n `18`; unknown avg `-0.1519` n `517`
- 24h: commodity avg `-1.4641` n `12`; crypto_alt avg `1.4755` n `228`; crypto_major avg `1.9082` n `8`; equity avg `3.4582` n `74`; fx avg `-0.2646` n `6`; index avg `1.4265` n `23`; metal avg `1.2541` n `18`; unknown avg `-2.8752` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
