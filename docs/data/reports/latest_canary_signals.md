# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T13:07:28.329639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `0.1499` n `230`; crypto_major avg `0.153` n `8`; equity avg `-0.0244` n `100`; fx avg `0.0016` n `6`; index avg `0.0054` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0075` n `774`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.297` n `230`; crypto_major avg `0.1765` n `8`; equity avg `-0.0324` n `100`; fx avg `-0.0014` n `6`; index avg `0.0026` n `25`; metal avg `0.0027` n `20`; unknown avg `0.0252` n `774`
- 4h: commodity avg `-0.0956` n `12`; crypto_alt avg `0.4767` n `230`; crypto_major avg `0.5116` n `8`; equity avg `0.0433` n `100`; fx avg `-0.0251` n `6`; index avg `0.0213` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.0066` n `774`
- 24h: commodity avg `-0.2807` n `12`; crypto_alt avg `0.0997` n `230`; crypto_major avg `0.1911` n `8`; equity avg `-2.6022` n `100`; fx avg `-0.0048` n `6`; index avg `-0.1866` n `25`; metal avg `0.0117` n `20`; unknown avg `13.2674` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1626`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1547`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1251`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1221`, n `667`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1152`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1136`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1055`, n `667`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `669`, weak_sample_signal
