# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T07:07:28.493075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0919` n `12`; crypto_alt avg `0.2014` n `230`; crypto_major avg `0.0936` n `8`; equity avg `0.0106` n `100`; fx avg `0.002` n `6`; index avg `0.0022` n `25`; metal avg `0.0045` n `20`; unknown avg `0.0176` n `775`
- 1h: commodity avg `0.0162` n `12`; crypto_alt avg `0.2418` n `230`; crypto_major avg `0.1529` n `8`; equity avg `0.0852` n `100`; fx avg `0.0031` n `6`; index avg `0.0021` n `25`; metal avg `0.0045` n `20`; unknown avg `0.0229` n `775`
- 4h: commodity avg `-0.0434` n `12`; crypto_alt avg `0.622` n `230`; crypto_major avg `0.3814` n `8`; equity avg `0.107` n `100`; fx avg `0.0707` n `6`; index avg `0.007` n `25`; metal avg `0.0155` n `20`; unknown avg `0.0584` n `758`
- 24h: commodity avg `-0.5527` n `12`; crypto_alt avg `1.6416` n `230`; crypto_major avg `1.8136` n `8`; equity avg `0.5342` n `100`; fx avg `0.0539` n `6`; index avg `0.1272` n `25`; metal avg `0.053` n `20`; unknown avg `-0.0922` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1395`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1242`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1217`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1209`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
