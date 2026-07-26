# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T09:37:15.058517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `-0.0462` n `8`; equity avg `0.0095` n `100`; fx avg `0.0` n `6`; index avg `0.0088` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.0002` n `775`
- 1h: commodity avg `-0.0518` n `12`; crypto_alt avg `-0.1086` n `230`; crypto_major avg `0.078` n `8`; equity avg `0.0845` n `100`; fx avg `-0.0021` n `6`; index avg `0.0101` n `25`; metal avg `0.0237` n `20`; unknown avg `-0.0439` n `775`
- 4h: commodity avg `-0.09` n `12`; crypto_alt avg `0.1801` n `230`; crypto_major avg `-0.0259` n `8`; equity avg `0.0546` n `100`; fx avg `-0.0384` n `6`; index avg `0.0252` n `25`; metal avg `0.065` n `20`; unknown avg `-0.0464` n `759`
- 24h: commodity avg `-0.6802` n `12`; crypto_alt avg `1.5929` n `230`; crypto_major avg `1.729` n `8`; equity avg `0.6223` n `100`; fx avg `0.0038` n `6`; index avg `0.1332` n `25`; metal avg `0.0942` n `20`; unknown avg `0.049` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1455`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1308`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1304`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1216`, n `666`, weak_sample_signal
