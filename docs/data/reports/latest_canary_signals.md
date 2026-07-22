# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T03:52:26.838905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `12`; crypto_alt avg `0.0417` n `230`; crypto_major avg `0.1444` n `8`; equity avg `-0.0347` n `98`; fx avg `0.0031` n `6`; index avg `-0.0259` n `25`; metal avg `-0.0287` n `20`; unknown avg `-0.0049` n `771`
- 1h: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.1799` n `230`; crypto_major avg `-0.1072` n `8`; equity avg `-0.1986` n `98`; fx avg `0.0332` n `6`; index avg `-0.0638` n `25`; metal avg `0.045` n `20`; unknown avg `-0.2034` n `771`
- 4h: commodity avg `0.0541` n `12`; crypto_alt avg `-0.1069` n `230`; crypto_major avg `-0.0916` n `8`; equity avg `-0.6089` n `98`; fx avg `0.0317` n `6`; index avg `-0.0627` n `25`; metal avg `0.4125` n `20`; unknown avg `-0.2989` n `771`
- 24h: commodity avg `0.5823` n `12`; crypto_alt avg `0.0857` n `230`; crypto_major avg `-0.0281` n `8`; equity avg `2.2691` n `98`; fx avg `0.1006` n `6`; index avg `0.2719` n `25`; metal avg `0.8296` n `20`; unknown avg `0.3083` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0942`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0594`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0538`, n `666`, weak_sample_signal
