# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T15:07:29.017115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `-0.1753` n `230`; crypto_major avg `-0.2342` n `8`; equity avg `-0.4586` n `100`; fx avg `0.0021` n `6`; index avg `-0.0363` n `25`; metal avg `-0.0381` n `20`; unknown avg `0.0204` n `772`
- 1h: commodity avg `0.0566` n `12`; crypto_alt avg `-0.1652` n `230`; crypto_major avg `-0.3102` n `8`; equity avg `-1.2924` n `100`; fx avg `-0.015` n `6`; index avg `-0.1649` n `25`; metal avg `0.0168` n `20`; unknown avg `-0.0427` n `772`
- 4h: commodity avg `0.2038` n `12`; crypto_alt avg `-0.6286` n `230`; crypto_major avg `-1.3445` n `8`; equity avg `-1.7102` n `99`; fx avg `-0.0071` n `6`; index avg `-0.3869` n `25`; metal avg `-0.3327` n `20`; unknown avg `0.2334` n `772`
- 24h: commodity avg `0.9626` n `12`; crypto_alt avg `-1.2072` n `230`; crypto_major avg `-1.6411` n `8`; equity avg `-2.0993` n `99`; fx avg `-0.0714` n `6`; index avg `-0.3882` n `25`; metal avg `-0.8638` n `20`; unknown avg `-0.2123` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
