# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T00:52:31.829525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `0.0306` n `233`; crypto_major avg `-0.0977` n `8`; equity avg `-0.004` n `136`; fx avg `-0.0051` n `6`; index avg `0.0002` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.2988` n `836`
- 1h: commodity avg `-0.0142` n `12`; crypto_alt avg `0.4386` n `233`; crypto_major avg `-0.1743` n `8`; equity avg `0.0819` n `136`; fx avg `-0.0064` n `6`; index avg `0.0311` n `26`; metal avg `0.0049` n `20`; unknown avg `0.2467` n `828`
- 4h: commodity avg `-0.0753` n `12`; crypto_alt avg `0.1449` n `233`; crypto_major avg `-0.445` n `8`; equity avg `0.0953` n `136`; fx avg `-0.019` n `6`; index avg `0.0373` n `26`; metal avg `-0.0143` n `20`; unknown avg `0.4091` n `814`
- 24h: commodity avg `-0.7186` n `12`; crypto_alt avg `1.1371` n `233`; crypto_major avg `1.2926` n `8`; equity avg `0.8321` n `136`; fx avg `-0.1942` n `6`; index avg `0.3231` n `26`; metal avg `0.1902` n `20`; unknown avg `0.9905` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
