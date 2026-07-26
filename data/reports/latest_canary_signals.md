# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T02:52:24.508005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `0.1314` n `230`; crypto_major avg `0.0764` n `8`; equity avg `0.0193` n `100`; fx avg `0.0026` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.0441` n `774`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `0.1389` n `230`; crypto_major avg `0.164` n `8`; equity avg `-0.0009` n `100`; fx avg `0.0046` n `6`; index avg `-0.0024` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0605` n `774`
- 4h: commodity avg `0.0297` n `12`; crypto_alt avg `0.1473` n `230`; crypto_major avg `0.2719` n `8`; equity avg `0.1825` n `100`; fx avg `0.0046` n `6`; index avg `0.0329` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.2814` n `774`
- 24h: commodity avg `-0.4811` n `12`; crypto_alt avg `0.8209` n `230`; crypto_major avg `1.4026` n `8`; equity avg `0.498` n `100`; fx avg `-0.0004` n `6`; index avg `0.1385` n `25`; metal avg `0.0322` n `20`; unknown avg `-0.213` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1376`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1232`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1213`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1183`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.118`, n `666`, weak_sample_signal
