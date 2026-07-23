# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T12:37:26.226986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0536` n `12`; crypto_alt avg `-0.4721` n `230`; crypto_major avg `-0.6541` n `8`; equity avg `-0.426` n `99`; fx avg `0.0191` n `6`; index avg `-0.0826` n `25`; metal avg `-0.0759` n `20`; unknown avg `0.0523` n `772`
- 1h: commodity avg `0.1072` n `12`; crypto_alt avg `-0.3787` n `230`; crypto_major avg `-0.6507` n `8`; equity avg `-0.7142` n `99`; fx avg `0.0376` n `6`; index avg `-0.1483` n `25`; metal avg `-0.1415` n `20`; unknown avg `0.1303` n `772`
- 4h: commodity avg `0.2607` n `12`; crypto_alt avg `-0.4728` n `230`; crypto_major avg `-0.5913` n `8`; equity avg `-1.1359` n `99`; fx avg `-0.0186` n `6`; index avg `-0.2198` n `25`; metal avg `-0.2695` n `20`; unknown avg `0.0306` n `772`
- 24h: commodity avg `0.9467` n `12`; crypto_alt avg `-0.4761` n `230`; crypto_major avg `-0.4817` n `8`; equity avg `-0.2147` n `99`; fx avg `-0.0743` n `6`; index avg `-0.0316` n `25`; metal avg `-0.663` n `20`; unknown avg `10.1671` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0688`, n `666`, weak_sample_signal
