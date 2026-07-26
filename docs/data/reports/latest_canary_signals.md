# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T02:37:30.403609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.0492` n `230`; crypto_major avg `-0.056` n `8`; equity avg `-0.0232` n `100`; fx avg `0.0003` n `6`; index avg `0.0013` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0163` n `774`
- 1h: commodity avg `0.0479` n `12`; crypto_alt avg `0.032` n `230`; crypto_major avg `0.1199` n `8`; equity avg `-0.0389` n `100`; fx avg `0.0065` n `6`; index avg `0.0051` n `25`; metal avg `0.0018` n `20`; unknown avg `0.0996` n `774`
- 4h: commodity avg `0.0579` n `12`; crypto_alt avg `0.0603` n `230`; crypto_major avg `0.2268` n `8`; equity avg `0.1675` n `100`; fx avg `-0.0013` n `6`; index avg `0.0388` n `25`; metal avg `0.0044` n `20`; unknown avg `-0.2785` n `774`
- 24h: commodity avg `-0.5259` n `12`; crypto_alt avg `0.6447` n `230`; crypto_major avg `1.2662` n `8`; equity avg `0.5421` n `100`; fx avg `-0.001` n `6`; index avg `0.165` n `25`; metal avg `0.0328` n `20`; unknown avg `-0.2339` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1821`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1368`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1231`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.118`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1175`, n `666`, weak_sample_signal
