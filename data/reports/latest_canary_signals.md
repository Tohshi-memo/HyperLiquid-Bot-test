# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T04:22:25.408084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0382` n `12`; crypto_alt avg `-0.0015` n `230`; crypto_major avg `-0.0054` n `8`; equity avg `0.0066` n `100`; fx avg `0.0284` n `6`; index avg `0.0006` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.0113` n `775`
- 1h: commodity avg `-0.0386` n `12`; crypto_alt avg `0.0046` n `230`; crypto_major avg `0.0524` n `8`; equity avg `0.0485` n `100`; fx avg `0.0586` n `6`; index avg `0.0122` n `25`; metal avg `0.0163` n `20`; unknown avg `0.3801` n `775`
- 4h: commodity avg `-0.069` n `12`; crypto_alt avg `0.3934` n `230`; crypto_major avg `0.3056` n `8`; equity avg `0.1892` n `100`; fx avg `0.0759` n `6`; index avg `0.0311` n `25`; metal avg `0.0209` n `20`; unknown avg `-0.0409` n `774`
- 24h: commodity avg `-0.5053` n `12`; crypto_alt avg `0.7461` n `230`; crypto_major avg `1.335` n `8`; equity avg `0.4359` n `100`; fx avg `0.0671` n `6`; index avg `0.137` n `25`; metal avg `0.0584` n `20`; unknown avg `-0.2235` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1835`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1373`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1247`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.122`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1173`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1161`, n `666`, weak_sample_signal
