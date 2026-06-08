# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T09:52:26.631639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0245` n `12`; crypto_alt avg `0.2117` n `228`; crypto_major avg `0.1118` n `8`; equity avg `0.0917` n `74`; fx avg `-0.0064` n `6`; index avg `0.1093` n `23`; metal avg `0.0309` n `18`; unknown avg `-0.009` n `517`
- 1h: commodity avg `-0.1032` n `12`; crypto_alt avg `0.8219` n `228`; crypto_major avg `0.6385` n `8`; equity avg `0.3466` n `74`; fx avg `-0.0028` n `6`; index avg `0.1175` n `23`; metal avg `0.1332` n `18`; unknown avg `0.0799` n `517`
- 4h: commodity avg `-0.2749` n `12`; crypto_alt avg `1.4111` n `228`; crypto_major avg `0.9457` n `8`; equity avg `1.1045` n `74`; fx avg `-0.1856` n `6`; index avg `0.4157` n `23`; metal avg `0.4288` n `18`; unknown avg `-0.0951` n `507`
- 24h: commodity avg `0.7744` n `12`; crypto_alt avg `0.1668` n `228`; crypto_major avg `1.3134` n `8`; equity avg `0.8987` n `74`; fx avg `-0.338` n `6`; index avg `0.4525` n `23`; metal avg `-0.7945` n `18`; unknown avg `-4.5517` n `506`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
