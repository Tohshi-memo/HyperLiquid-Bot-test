# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T05:37:23.835432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.0816` n `230`; crypto_major avg `-0.0192` n `8`; equity avg `-0.0737` n `100`; fx avg `0.018` n `6`; index avg `-0.0319` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.1437` n `772`
- 1h: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.0008` n `230`; crypto_major avg `0.0172` n `8`; equity avg `0.2537` n `100`; fx avg `-0.011` n `6`; index avg `0.0415` n `25`; metal avg `0.0212` n `20`; unknown avg `0.2129` n `772`
- 4h: commodity avg `0.0731` n `12`; crypto_alt avg `0.1297` n `230`; crypto_major avg `0.0144` n `8`; equity avg `-0.4404` n `100`; fx avg `-0.0094` n `6`; index avg `-0.1573` n `25`; metal avg `-0.1145` n `20`; unknown avg `-0.3047` n `772`
- 24h: commodity avg `0.5156` n `12`; crypto_alt avg `-1.1988` n `230`; crypto_major avg `-1.7628` n `8`; equity avg `-2.1447` n `99`; fx avg `-0.0969` n `6`; index avg `-0.5987` n `25`; metal avg `-1.0257` n `20`; unknown avg `0.0213` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1053`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0906`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0869`, n `666`, weak_sample_signal
