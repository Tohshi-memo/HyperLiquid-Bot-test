# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T18:22:31.118694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.0925` n `230`; crypto_major avg `-0.1009` n `8`; equity avg `-0.011` n `100`; fx avg `0.003` n `6`; index avg `-0.0082` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.13` n `774`
- 1h: commodity avg `-0.094` n `12`; crypto_alt avg `0.0893` n `230`; crypto_major avg `0.1314` n `8`; equity avg `0.0502` n `100`; fx avg `-0.0212` n `6`; index avg `0.0319` n `25`; metal avg `0.0121` n `20`; unknown avg `-0.0202` n `774`
- 4h: commodity avg `-0.1127` n `12`; crypto_alt avg `0.775` n `230`; crypto_major avg `1.17` n `8`; equity avg `0.2122` n `100`; fx avg `-0.0184` n `6`; index avg `0.0452` n `25`; metal avg `0.0177` n `20`; unknown avg `0.017` n `774`
- 24h: commodity avg `-0.4155` n `12`; crypto_alt avg `0.4971` n `230`; crypto_major avg `1.177` n `8`; equity avg `-0.188` n `100`; fx avg `-0.0218` n `6`; index avg `0.0231` n `25`; metal avg `-0.0302` n `20`; unknown avg `-0.2609` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.168`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1297`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1187`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1125`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1116`, n `666`, weak_sample_signal
