# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T07:37:31.831573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.68` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0707` n `12`; crypto_alt avg `-0.2563` n `228`; crypto_major avg `-0.2521` n `8`; equity avg `-0.0696` n `74`; fx avg `0.0055` n `6`; index avg `-0.0061` n `23`; metal avg `-0.078` n `18`; unknown avg `0.2599` n `689`
- 1h: commodity avg `-0.4019` n `12`; crypto_alt avg `-0.1483` n `228`; crypto_major avg `0.0021` n `8`; equity avg `0.1158` n `74`; fx avg `-0.0099` n `6`; index avg `0.2509` n `23`; metal avg `0.0653` n `18`; unknown avg `0.5073` n `689`
- 4h: commodity avg `-0.3963` n `12`; crypto_alt avg `0.144` n `228`; crypto_major avg `-0.0985` n `8`; equity avg `0.0016` n `74`; fx avg `0.0286` n `6`; index avg `0.0551` n `23`; metal avg `-0.2295` n `18`; unknown avg `0.036` n `529`
- 24h: commodity avg `-1.1793` n `12`; crypto_alt avg `2.9836` n `228`; crypto_major avg `2.8528` n `8`; equity avg `1.7845` n `74`; fx avg `0.0441` n `6`; index avg `0.9819` n `23`; metal avg `1.7593` n `18`; unknown avg `1.6775` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
