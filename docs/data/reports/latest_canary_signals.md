# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T13:22:25.781031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0413` n `12`; crypto_alt avg `0.3345` n `230`; crypto_major avg `0.3617` n `8`; equity avg `0.0113` n `100`; fx avg `0.001` n `6`; index avg `0.0149` n `25`; metal avg `-0.0244` n `20`; unknown avg `0.182` n `773`
- 1h: commodity avg `0.1776` n `12`; crypto_alt avg `-0.812` n `230`; crypto_major avg `-0.5896` n `8`; equity avg `-0.4002` n `100`; fx avg `-0.0013` n `6`; index avg `-0.0931` n `25`; metal avg `-0.2088` n `20`; unknown avg `-0.0402` n `773`
- 4h: commodity avg `0.3754` n `12`; crypto_alt avg `-1.0021` n `230`; crypto_major avg `-0.7352` n `8`; equity avg `-0.2315` n `100`; fx avg `-0.0184` n `6`; index avg `-0.0403` n `25`; metal avg `-0.1354` n `20`; unknown avg `-0.0776` n `773`
- 24h: commodity avg `-0.0603` n `12`; crypto_alt avg `-1.6041` n `230`; crypto_major avg `-1.6105` n `8`; equity avg `-0.4002` n `100`; fx avg `-0.1595` n `6`; index avg `-0.1622` n `25`; metal avg `-0.1035` n `20`; unknown avg `0.2104` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1009`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0914`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0839`, n `666`, weak_sample_signal
