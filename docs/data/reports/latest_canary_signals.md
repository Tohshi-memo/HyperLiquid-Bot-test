# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T07:52:24.115300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.0087` n `230`; crypto_major avg `-0.005` n `8`; equity avg `0.0087` n `100`; fx avg `0.0024` n `6`; index avg `-0.0088` n `25`; metal avg `-0.003` n `20`; unknown avg `-0.0128` n `774`
- 1h: commodity avg `0.0265` n `12`; crypto_alt avg `0.0553` n `230`; crypto_major avg `-0.0256` n `8`; equity avg `-0.0454` n `100`; fx avg `0.0159` n `6`; index avg `-0.012` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.1881` n `774`
- 4h: commodity avg `0.0577` n `12`; crypto_alt avg `-0.2709` n `230`; crypto_major avg `-0.2205` n `8`; equity avg `-0.0242` n `100`; fx avg `0.0206` n `6`; index avg `0.0131` n `25`; metal avg `0.0118` n `20`; unknown avg `-0.2356` n `758`
- 24h: commodity avg `-0.1054` n `12`; crypto_alt avg `-1.8611` n `230`; crypto_major avg `-1.6969` n `8`; equity avg `-2.7927` n `100`; fx avg `-0.0679` n `6`; index avg `-0.2259` n `25`; metal avg `-0.0094` n `20`; unknown avg `13.4402` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1148`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1065`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.106`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
