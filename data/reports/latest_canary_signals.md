# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T14:07:25.537405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1218` n `12`; crypto_alt avg `-0.2006` n `228`; crypto_major avg `-0.1135` n `8`; equity avg `-0.109` n `74`; fx avg `0.0117` n `6`; index avg `-0.0656` n `23`; metal avg `-0.3183` n `18`; unknown avg `-0.0358` n `517`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.3849` n `228`; crypto_major avg `-0.0514` n `8`; equity avg `-0.522` n `74`; fx avg `0.0222` n `6`; index avg `-0.2347` n `23`; metal avg `-0.4813` n `18`; unknown avg `0.0942` n `517`
- 4h: commodity avg `-0.9122` n `12`; crypto_alt avg `0.8532` n `228`; crypto_major avg `0.9731` n `8`; equity avg `0.8418` n `74`; fx avg `0.0597` n `6`; index avg `0.558` n `23`; metal avg `0.2186` n `18`; unknown avg `-1.5784` n `517`
- 24h: commodity avg `-0.2951` n `12`; crypto_alt avg `2.3421` n `228`; crypto_major avg `3.6018` n `8`; equity avg `1.8445` n `74`; fx avg `-0.2619` n `6`; index avg `0.8946` n `23`; metal avg `-0.3758` n `18`; unknown avg `-2.7834` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
