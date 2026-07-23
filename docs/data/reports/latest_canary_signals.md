# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T20:52:30.365130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0745` n `12`; crypto_alt avg `-0.0973` n `230`; crypto_major avg `-0.0823` n `8`; equity avg `-0.0519` n `100`; fx avg `-0.0025` n `6`; index avg `-0.0198` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.1743` n `772`
- 1h: commodity avg `0.0915` n `12`; crypto_alt avg `0.4956` n `230`; crypto_major avg `0.6016` n `8`; equity avg `0.7784` n `100`; fx avg `0.0021` n `6`; index avg `0.13` n `25`; metal avg `0.0229` n `20`; unknown avg `0.4299` n `772`
- 4h: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.2461` n `230`; crypto_major avg `-0.0334` n `8`; equity avg `0.0501` n `100`; fx avg `0.014` n `6`; index avg `0.0741` n `25`; metal avg `-0.036` n `20`; unknown avg `-0.3098` n `772`
- 24h: commodity avg `0.9323` n `12`; crypto_alt avg `-1.3903` n `230`; crypto_major avg `-1.8594` n `8`; equity avg `-0.9766` n `99`; fx avg `-0.0733` n `6`; index avg `-0.2338` n `25`; metal avg `-0.7748` n `20`; unknown avg `-0.3336` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
