# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T14:04:57.924059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.107` n `12`; crypto_alt avg `-0.3658` n `228`; crypto_major avg `-0.2831` n `8`; equity avg `-0.1572` n `67`; fx avg `0.0017` n `6`; index avg `-0.02` n `23`; metal avg `0.0023` n `18`; unknown avg `-0.1396` n `396`
- 1h: commodity avg `0.2223` n `12`; crypto_alt avg `-0.5743` n `228`; crypto_major avg `-0.5381` n `8`; equity avg `-0.251` n `67`; fx avg `0.0136` n `6`; index avg `-0.0439` n `23`; metal avg `-0.0947` n `18`; unknown avg `-0.0342` n `396`
- 4h: commodity avg `0.2748` n `12`; crypto_alt avg `-0.9493` n `228`; crypto_major avg `-0.3976` n `8`; equity avg `0.0218` n `67`; fx avg `0.0254` n `6`; index avg `-0.1361` n `23`; metal avg `-0.3014` n `18`; unknown avg `0.6956` n `396`
- 24h: commodity avg `-2.2546` n `12`; crypto_alt avg `1.7697` n `228`; crypto_major avg `3.5903` n `8`; equity avg `2.2956` n `67`; fx avg `0.0873` n `6`; index avg `0.9684` n `23`; metal avg `1.0137` n `18`; unknown avg `1.6478` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
