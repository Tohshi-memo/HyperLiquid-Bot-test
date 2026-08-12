# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T19:52:27.804972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `-0.0496` n `230`; crypto_major avg `-0.1098` n `8`; equity avg `0.0268` n `113`; fx avg `0.0032` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0121` n `20`; unknown avg `-0.1494` n `786`
- 1h: commodity avg `-0.028` n `12`; crypto_alt avg `-0.3237` n `230`; crypto_major avg `-0.2557` n `8`; equity avg `-0.1163` n `113`; fx avg `0.0013` n `6`; index avg `-0.022` n `25`; metal avg `-0.0617` n `20`; unknown avg `-0.2947` n `786`
- 4h: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.3989` n `230`; crypto_major avg `-0.3363` n `8`; equity avg `0.4152` n `113`; fx avg `-0.003` n `6`; index avg `0.0379` n `25`; metal avg `-0.094` n `20`; unknown avg `-0.0396` n `786`
- 24h: commodity avg `0.0029` n `12`; crypto_alt avg `-0.6907` n `230`; crypto_major avg `0.2513` n `8`; equity avg `3.5801` n `113`; fx avg `0.0228` n `6`; index avg `0.4163` n `25`; metal avg `0.193` n `20`; unknown avg `0.0359` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
