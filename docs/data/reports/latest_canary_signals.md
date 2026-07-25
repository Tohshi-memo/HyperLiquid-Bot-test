# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T15:16:46.647340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.0576` n `230`; crypto_major avg `0.1326` n `8`; equity avg `-0.0016` n `100`; fx avg `-0.0061` n `6`; index avg `-0.0081` n `25`; metal avg `0.0011` n `20`; unknown avg `0.2697` n `774`
- 1h: commodity avg `0.0058` n `12`; crypto_alt avg `0.1772` n `230`; crypto_major avg `0.4704` n `8`; equity avg `0.0554` n `100`; fx avg `0.0025` n `6`; index avg `-0.0076` n `25`; metal avg `0.0186` n `20`; unknown avg `-0.0026` n `774`
- 4h: commodity avg `-0.341` n `12`; crypto_alt avg `0.3463` n `230`; crypto_major avg `0.5518` n `8`; equity avg `0.0339` n `100`; fx avg `-0.0033` n `6`; index avg `-0.0086` n `25`; metal avg `0.024` n `20`; unknown avg `0.0231` n `774`
- 24h: commodity avg `-0.3349` n `12`; crypto_alt avg `-0.0613` n `230`; crypto_major avg `0.3784` n `8`; equity avg `-1.0687` n `100`; fx avg `-0.0258` n `6`; index avg `-0.1752` n `25`; metal avg `-0.188` n `20`; unknown avg `-0.3947` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1244`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1151`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1085`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
