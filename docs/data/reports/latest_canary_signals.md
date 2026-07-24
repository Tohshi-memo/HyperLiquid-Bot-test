# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T02:22:24.361607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `12`; crypto_alt avg `0.0113` n `230`; crypto_major avg `0.0092` n `8`; equity avg `-0.1203` n `100`; fx avg `-0.0098` n `6`; index avg `-0.0243` n `25`; metal avg `0.009` n `20`; unknown avg `-0.1388` n `772`
- 1h: commodity avg `0.0767` n `12`; crypto_alt avg `0.1813` n `230`; crypto_major avg `0.0669` n `8`; equity avg `-0.2517` n `100`; fx avg `-0.0264` n `6`; index avg `-0.0918` n `25`; metal avg `-0.0047` n `20`; unknown avg `-0.147` n `772`
- 4h: commodity avg `-0.03` n `12`; crypto_alt avg `0.0893` n `230`; crypto_major avg `-0.0834` n `8`; equity avg `-0.4637` n `100`; fx avg `-0.11` n `6`; index avg `-0.167` n `25`; metal avg `-0.0873` n `20`; unknown avg `-0.5242` n `772`
- 24h: commodity avg `0.5441` n `12`; crypto_alt avg `-1.2134` n `230`; crypto_major avg `-1.8241` n `8`; equity avg `-1.5922` n `99`; fx avg `-0.1053` n `6`; index avg `-0.458` n `25`; metal avg `-0.8533` n `20`; unknown avg `-0.3415` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0946`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0872`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
