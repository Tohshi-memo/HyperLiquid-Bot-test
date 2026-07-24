# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T01:37:24.804450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `12`; crypto_alt avg `0.1973` n `230`; crypto_major avg `0.2056` n `8`; equity avg `0.1085` n `100`; fx avg `-0.0034` n `6`; index avg `0.0271` n `25`; metal avg `0.0149` n `20`; unknown avg `0.1162` n `772`
- 1h: commodity avg `-0.1333` n `12`; crypto_alt avg `0.5352` n `230`; crypto_major avg `0.4213` n `8`; equity avg `0.3327` n `100`; fx avg `-0.0561` n `6`; index avg `0.0722` n `25`; metal avg `-0.0724` n `20`; unknown avg `0.0824` n `772`
- 4h: commodity avg `-0.1514` n `12`; crypto_alt avg `-0.0555` n `230`; crypto_major avg `0.0602` n `8`; equity avg `-0.2416` n `100`; fx avg `-0.0842` n `6`; index avg `-0.1066` n `25`; metal avg `-0.1057` n `20`; unknown avg `-0.3476` n `772`
- 24h: commodity avg `0.4824` n `12`; crypto_alt avg `-1.3868` n `230`; crypto_major avg `-1.8573` n `8`; equity avg `-1.8909` n `99`; fx avg `-0.105` n `6`; index avg `-0.4718` n `25`; metal avg `-0.8539` n `20`; unknown avg `-0.3548` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0858`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
