# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T15:52:26.558589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0756` n `12`; crypto_alt avg `-0.1189` n `230`; crypto_major avg `-0.1577` n `8`; equity avg `0.1294` n `100`; fx avg `-0.0035` n `6`; index avg `0.0208` n `25`; metal avg `0.0367` n `20`; unknown avg `-0.0624` n `773`
- 1h: commodity avg `-0.1909` n `12`; crypto_alt avg `0.3099` n `230`; crypto_major avg `0.2529` n `8`; equity avg `0.8932` n `100`; fx avg `0.0422` n `6`; index avg `0.1845` n `25`; metal avg `0.1832` n `20`; unknown avg `-0.1177` n `773`
- 4h: commodity avg `-0.1425` n `12`; crypto_alt avg `-0.7359` n `230`; crypto_major avg `-0.6933` n `8`; equity avg `-1.6442` n `100`; fx avg `0.0331` n `6`; index avg `-0.0506` n `25`; metal avg `0.1446` n `20`; unknown avg `13.0922` n `773`
- 24h: commodity avg `-0.5064` n `12`; crypto_alt avg `-1.574` n `230`; crypto_major avg `-1.4373` n `8`; equity avg `-1.7657` n `100`; fx avg `-0.0996` n `6`; index avg `-0.0999` n `25`; metal avg `0.1869` n `20`; unknown avg `13.5287` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1157`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1146`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1034`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
