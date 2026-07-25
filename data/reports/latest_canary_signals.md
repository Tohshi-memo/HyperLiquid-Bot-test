# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T13:22:30.387770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `-0.0106` n `230`; crypto_major avg `0.0127` n `8`; equity avg `-0.0168` n `100`; fx avg `0.0048` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0278` n `774`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `0.2825` n `230`; crypto_major avg `0.253` n `8`; equity avg `-0.0283` n `100`; fx avg `0.0059` n `6`; index avg `0.0002` n `25`; metal avg `-0.0032` n `20`; unknown avg `-0.0034` n `774`
- 4h: commodity avg `-0.072` n `12`; crypto_alt avg `0.4214` n `230`; crypto_major avg `0.3992` n `8`; equity avg `0.006` n `100`; fx avg `-0.0195` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0046` n `20`; unknown avg `-0.0366` n `774`
- 24h: commodity avg `-0.3058` n `12`; crypto_alt avg `-0.2431` n `230`; crypto_major avg `-0.1578` n `8`; equity avg `-2.6275` n `100`; fx avg `-0.001` n `6`; index avg `-0.2079` n `25`; metal avg `0.0328` n `20`; unknown avg `13.2443` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1634`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.156`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1261`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1235`, n `667`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1067`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1031`, n `667`, weak_sample_signal
