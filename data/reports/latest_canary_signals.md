# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T00:37:28.480143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.0437` n `230`; crypto_major avg `0.0594` n `8`; equity avg `-0.0075` n `100`; fx avg `0.0099` n `6`; index avg `-0.007` n `25`; metal avg `0.0012` n `20`; unknown avg `0.0589` n `774`
- 1h: commodity avg `-0.0879` n `12`; crypto_alt avg `0.1827` n `230`; crypto_major avg `0.1493` n `8`; equity avg `0.1654` n `100`; fx avg `-0.016` n `6`; index avg `0.0455` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0681` n `774`
- 4h: commodity avg `-0.0787` n `12`; crypto_alt avg `-0.0356` n `230`; crypto_major avg `0.01` n `8`; equity avg `-0.0824` n `100`; fx avg `0.0269` n `6`; index avg `0.0259` n `25`; metal avg `0.0153` n `20`; unknown avg `-0.176` n `774`
- 24h: commodity avg `-0.4019` n `12`; crypto_alt avg `-0.385` n `230`; crypto_major avg `-0.5064` n `8`; equity avg `-2.8017` n `100`; fx avg `-0.1054` n `6`; index avg `-0.299` n `25`; metal avg `0.0122` n `20`; unknown avg `14.0159` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1266`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1189`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1105`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
