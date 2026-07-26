# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T22:07:32.138813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.309` n `12`; crypto_alt avg `0.409` n `230`; crypto_major avg `0.3783` n `8`; equity avg `0.2657` n `100`; fx avg `0.0067` n `6`; index avg `0.1036` n `25`; metal avg `0.149` n `20`; unknown avg `-0.0972` n `775`
- 1h: commodity avg `-0.4958` n `12`; crypto_alt avg `0.7339` n `230`; crypto_major avg `0.716` n `8`; equity avg `0.3354` n `100`; fx avg `0.0128` n `6`; index avg `0.1048` n `25`; metal avg `0.1904` n `20`; unknown avg `-0.0411` n `775`
- 4h: commodity avg `-0.2395` n `12`; crypto_alt avg `0.5893` n `230`; crypto_major avg `0.627` n `8`; equity avg `0.3003` n `100`; fx avg `0.0261` n `6`; index avg `0.0616` n `25`; metal avg `0.2088` n `20`; unknown avg `-0.3116` n `775`
- 24h: commodity avg `-0.6499` n `12`; crypto_alt avg `1.3363` n `230`; crypto_major avg `1.5249` n `8`; equity avg `0.9556` n `100`; fx avg `0.0525` n `6`; index avg `0.1975` n `25`; metal avg `0.3949` n `20`; unknown avg `0.0669` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
