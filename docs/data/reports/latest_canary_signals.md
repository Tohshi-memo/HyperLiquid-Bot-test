# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T10:07:24.618539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2048` n `12`; crypto_alt avg `0.0256` n `230`; crypto_major avg `0.0101` n `8`; equity avg `0.0301` n `100`; fx avg `-0.0025` n `6`; index avg `0.0098` n `25`; metal avg `0.0031` n `20`; unknown avg `0.0114` n `775`
- 1h: commodity avg `-0.3102` n `12`; crypto_alt avg `-0.0708` n `230`; crypto_major avg `0.0438` n `8`; equity avg `0.0949` n `100`; fx avg `-0.0025` n `6`; index avg `0.0248` n `25`; metal avg `0.027` n `20`; unknown avg `-0.025` n `775`
- 4h: commodity avg `-0.3657` n `12`; crypto_alt avg `0.0934` n `230`; crypto_major avg `0.0984` n `8`; equity avg `0.092` n `100`; fx avg `-0.0455` n `6`; index avg `0.0255` n `25`; metal avg `0.0769` n `20`; unknown avg `-0.0869` n `775`
- 24h: commodity avg `-0.9028` n `12`; crypto_alt avg `1.5781` n `230`; crypto_major avg `1.6418` n `8`; equity avg `0.6096` n `100`; fx avg `0.0042` n `6`; index avg `0.1454` n `25`; metal avg `0.1214` n `20`; unknown avg `0.0525` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1458`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1331`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1307`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1241`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1231`, n `666`, weak_sample_signal
