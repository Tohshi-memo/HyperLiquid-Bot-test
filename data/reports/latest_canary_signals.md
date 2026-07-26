# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T14:07:32.834007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `0.1412` n `230`; crypto_major avg `0.274` n `8`; equity avg `0.0879` n `100`; fx avg `0.0` n `6`; index avg `0.019` n `25`; metal avg `0.0191` n `20`; unknown avg `0.0018` n `775`
- 1h: commodity avg `0.0017` n `12`; crypto_alt avg `0.0948` n `230`; crypto_major avg `0.3834` n `8`; equity avg `0.1606` n `100`; fx avg `-0.0036` n `6`; index avg `0.0242` n `25`; metal avg `0.0303` n `20`; unknown avg `0.0177` n `775`
- 4h: commodity avg `0.0723` n `12`; crypto_alt avg `-0.0049` n `230`; crypto_major avg `0.1718` n `8`; equity avg `0.2626` n `100`; fx avg `0.0086` n `6`; index avg `0.0474` n `25`; metal avg `0.0908` n `20`; unknown avg `-0.0859` n `775`
- 24h: commodity avg `-0.4268` n `12`; crypto_alt avg `1.3112` n `230`; crypto_major avg `1.7004` n `8`; equity avg `0.9038` n `100`; fx avg `0.0196` n `6`; index avg `0.1899` n `25`; metal avg `0.2047` n `20`; unknown avg `0.0735` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
