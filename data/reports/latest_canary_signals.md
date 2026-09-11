# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T02:37:36.041795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `12`; crypto_alt avg `-0.0184` n `233`; crypto_major avg `-0.0333` n `8`; equity avg `-0.1862` n `136`; fx avg `-0.0008` n `6`; index avg `-0.0415` n `26`; metal avg `-0.0855` n `20`; unknown avg `-0.2544` n `796`
- 1h: commodity avg `0.0447` n `12`; crypto_alt avg `-0.1624` n `233`; crypto_major avg `0.0695` n `8`; equity avg `-0.2792` n `136`; fx avg `-0.0162` n `6`; index avg `-0.0274` n `26`; metal avg `-0.1179` n `20`; unknown avg `-0.341` n `788`
- 4h: commodity avg `-0.2489` n `12`; crypto_alt avg `-0.4774` n `233`; crypto_major avg `-0.3534` n `8`; equity avg `-0.1446` n `136`; fx avg `-0.027` n `6`; index avg `0.0018` n `26`; metal avg `-0.0371` n `20`; unknown avg `-0.4903` n `770`
- 24h: commodity avg `1.0691` n `12`; crypto_alt avg `-1.9642` n `233`; crypto_major avg `-2.2288` n `8`; equity avg `-1.8557` n `136`; fx avg `0.1095` n `6`; index avg `-0.3239` n `26`; metal avg `-1.379` n `20`; unknown avg `-1.0246` n `677`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
