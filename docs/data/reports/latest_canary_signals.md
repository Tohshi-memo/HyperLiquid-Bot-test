# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T21:07:31.396281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `0.0713` n `230`; crypto_major avg `0.005` n `8`; equity avg `0.3716` n `98`; fx avg `-0.0008` n `6`; index avg `0.0579` n `25`; metal avg `-0.0072` n `20`; unknown avg `0.1237` n `773`
- 1h: commodity avg `0.0301` n `12`; crypto_alt avg `0.2741` n `230`; crypto_major avg `0.1438` n `8`; equity avg `0.8373` n `98`; fx avg `0.0065` n `6`; index avg `0.0977` n `25`; metal avg `0.0049` n `20`; unknown avg `0.2062` n `773`
- 4h: commodity avg `0.0099` n `12`; crypto_alt avg `-0.4474` n `230`; crypto_major avg `-0.4744` n `8`; equity avg `-0.0872` n `98`; fx avg `0.0065` n `6`; index avg `-0.0252` n `25`; metal avg `-0.0977` n `20`; unknown avg `0.3288` n `773`
- 24h: commodity avg `0.467` n `12`; crypto_alt avg `-0.307` n `230`; crypto_major avg `-0.5991` n `8`; equity avg `-0.6723` n `98`; fx avg `-0.0351` n `6`; index avg `-0.0811` n `25`; metal avg `0.2574` n `20`; unknown avg `1.0516` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
