# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T04:07:24.062296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.0144` n `230`; crypto_major avg `-0.0097` n `8`; equity avg `0.0194` n `100`; fx avg `0.038` n `6`; index avg `0.0018` n `25`; metal avg `0.0055` n `20`; unknown avg `0.0309` n `775`
- 1h: commodity avg `-0.0262` n `12`; crypto_alt avg `0.1157` n `230`; crypto_major avg `0.136` n `8`; equity avg `0.0787` n `100`; fx avg `0.0412` n `6`; index avg `0.0123` n `25`; metal avg `0.0138` n `20`; unknown avg `0.2105` n `774`
- 4h: commodity avg `-0.0192` n `12`; crypto_alt avg `0.4128` n `230`; crypto_major avg `0.3775` n `8`; equity avg `0.1969` n `100`; fx avg `0.0422` n `6`; index avg `0.0314` n `25`; metal avg `0.0165` n `20`; unknown avg `-0.1284` n `774`
- 24h: commodity avg `-0.4554` n `12`; crypto_alt avg `0.8391` n `230`; crypto_major avg `1.3708` n `8`; equity avg `0.475` n `100`; fx avg `0.0383` n `6`; index avg `0.1527` n `25`; metal avg `0.0551` n `20`; unknown avg `-0.2191` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1374`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1247`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1175`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1161`, n `666`, weak_sample_signal
