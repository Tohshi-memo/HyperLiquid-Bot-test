# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T18:07:26.826122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.1613` n `230`; crypto_major avg `0.0798` n `8`; equity avg `0.0156` n `100`; fx avg `-0.0015` n `6`; index avg `0.0057` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.0673` n `774`
- 1h: commodity avg `-0.1169` n `12`; crypto_alt avg `0.3576` n `230`; crypto_major avg `0.4174` n `8`; equity avg `0.1482` n `100`; fx avg `-0.0284` n `6`; index avg `0.0468` n `25`; metal avg `0.0223` n `20`; unknown avg `-0.1059` n `774`
- 4h: commodity avg `-0.1127` n `12`; crypto_alt avg `0.8494` n `230`; crypto_major avg `1.2605` n `8`; equity avg `0.2337` n `100`; fx avg `-0.0287` n `6`; index avg `0.0574` n `25`; metal avg `0.0214` n `20`; unknown avg `-0.0027` n `774`
- 24h: commodity avg `-0.3557` n `12`; crypto_alt avg `0.4567` n `230`; crypto_major avg `1.1708` n `8`; equity avg `-0.4881` n `100`; fx avg `-0.0233` n `6`; index avg `-0.029` n `25`; metal avg `-0.0837` n `20`; unknown avg `-0.3066` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1295`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1186`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1123`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
