# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T21:37:28.032798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `0.0109` n `230`; crypto_major avg `-0.0368` n `8`; equity avg `-0.1085` n `100`; fx avg `0.0007` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0699` n `772`
- 1h: commodity avg `0.0861` n `12`; crypto_alt avg `-0.254` n `230`; crypto_major avg `-0.2478` n `8`; equity avg `-0.3073` n `100`; fx avg `-0.0134` n `6`; index avg `-0.0318` n `25`; metal avg `0.0203` n `20`; unknown avg `0.0582` n `772`
- 4h: commodity avg `-0.0782` n `12`; crypto_alt avg `-0.2537` n `230`; crypto_major avg `-0.1334` n `8`; equity avg `-0.1657` n `100`; fx avg `0.0039` n `6`; index avg `0.0812` n `25`; metal avg `0.0307` n `20`; unknown avg `0.075` n `772`
- 24h: commodity avg `0.8338` n `12`; crypto_alt avg `-1.6297` n `230`; crypto_major avg `-2.1544` n `8`; equity avg `-1.4323` n `99`; fx avg `-0.0725` n `6`; index avg `-0.2598` n `25`; metal avg `-0.7582` n `20`; unknown avg `-0.1672` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
