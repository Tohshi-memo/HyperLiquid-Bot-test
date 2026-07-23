# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T21:22:51.585514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0454` n `12`; crypto_alt avg `-0.1937` n `230`; crypto_major avg `-0.1318` n `8`; equity avg `-0.2055` n `100`; fx avg `0.0022` n `6`; index avg `-0.0205` n `25`; metal avg `-0.0076` n `20`; unknown avg `-0.2267` n `772`
- 1h: commodity avg `0.0653` n `12`; crypto_alt avg `-0.2684` n `230`; crypto_major avg `-0.2369` n `8`; equity avg `-0.2313` n `100`; fx avg `-0.0078` n `6`; index avg `-0.0302` n `25`; metal avg `0.0268` n `20`; unknown avg `0.178` n `772`
- 4h: commodity avg `-0.0726` n `12`; crypto_alt avg `-0.3475` n `230`; crypto_major avg `-0.2035` n `8`; equity avg `-0.1625` n `100`; fx avg `0.0051` n `6`; index avg `0.0504` n `25`; metal avg `-0.0154` n `20`; unknown avg `0.0465` n `772`
- 24h: commodity avg `0.8639` n `12`; crypto_alt avg `-1.5976` n `230`; crypto_major avg `-1.972` n `8`; equity avg `-1.4287` n `99`; fx avg `-0.0824` n `6`; index avg `-0.26` n `25`; metal avg `-0.7557` n `20`; unknown avg `-0.0519` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
