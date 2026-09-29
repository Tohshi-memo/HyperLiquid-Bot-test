# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T08:43:53.250512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.454` n `234`; crypto_major avg `-0.5469` n `8`; equity avg `-0.0701` n `141`; fx avg `-0.0255` n `6`; index avg `-0.0088` n `26`; metal avg `-0.0427` n `20`; unknown avg `2.1688` n `963`
- 1h: commodity avg `-0.1305` n `12`; crypto_alt avg `0.0168` n `234`; crypto_major avg `-0.2748` n `8`; equity avg `0.1781` n `141`; fx avg `0.0001` n `6`; index avg `0.0031` n `26`; metal avg `-0.0353` n `20`; unknown avg `0.2187` n `945`
- 4h: commodity avg `-0.3508` n `12`; crypto_alt avg `1.9` n `234`; crypto_major avg `1.1094` n `8`; equity avg `0.9975` n `141`; fx avg `-0.0568` n `6`; index avg `0.1424` n `26`; metal avg `0.0656` n `20`; unknown avg `1.4226` n `927`
- 24h: commodity avg `-0.395` n `12`; crypto_alt avg `1.1786` n `234`; crypto_major avg `0.9744` n `8`; equity avg `-0.0746` n `141`; fx avg `-0.0413` n `6`; index avg `-0.013` n `26`; metal avg `-0.1751` n `20`; unknown avg `55.533` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
