# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T17:22:29.565365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0331` n `12`; crypto_alt avg `0.0285` n `230`; crypto_major avg `-0.0113` n `8`; equity avg `-0.0042` n `100`; fx avg `0.0` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0089` n `20`; unknown avg `0.0809` n `775`
- 1h: commodity avg `0.0285` n `12`; crypto_alt avg `-0.0413` n `230`; crypto_major avg `-0.0264` n `8`; equity avg `0.0368` n `100`; fx avg `0.0012` n `6`; index avg `0.0013` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.1542` n `775`
- 4h: commodity avg `-0.0109` n `12`; crypto_alt avg `0.3793` n `230`; crypto_major avg `0.5265` n `8`; equity avg `0.1501` n `100`; fx avg `-0.0211` n `6`; index avg `0.0276` n `25`; metal avg `0.019` n `20`; unknown avg `0.1182` n `775`
- 24h: commodity avg `-0.4227` n `12`; crypto_alt avg `0.9426` n `230`; crypto_major avg `0.9413` n `8`; equity avg `0.787` n `100`; fx avg `0.0065` n `6`; index avg `0.1815` n `25`; metal avg `0.1886` n `20`; unknown avg `-0.037` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1941`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
