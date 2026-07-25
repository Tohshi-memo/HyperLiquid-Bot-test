# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T06:37:24.862995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.2035` n `230`; crypto_major avg `-0.1127` n `8`; equity avg `0.0051` n `100`; fx avg `0.0101` n `6`; index avg `0.0028` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.0216` n `774`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `-0.2781` n `230`; crypto_major avg `-0.1507` n `8`; equity avg `0.0254` n `100`; fx avg `0.0053` n `6`; index avg `0.006` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0295` n `758`
- 4h: commodity avg `-0.0834` n `12`; crypto_alt avg `-0.3594` n `230`; crypto_major avg `-0.2332` n `8`; equity avg `0.1649` n `100`; fx avg `0.0089` n `6`; index avg `0.0511` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.122` n `758`
- 24h: commodity avg `-0.2799` n `12`; crypto_alt avg `-1.9288` n `230`; crypto_major avg `-1.5827` n `8`; equity avg `-2.3553` n `100`; fx avg `-0.0807` n `6`; index avg `-0.1444` n `25`; metal avg `0.121` n `20`; unknown avg `13.6448` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1141`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1025`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
