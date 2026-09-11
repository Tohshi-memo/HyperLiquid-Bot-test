# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T23:07:28.343985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `0.151` n `233`; crypto_major avg `0.1337` n `8`; equity avg `0.0061` n `136`; fx avg `-0.0092` n `6`; index avg `0.0` n `26`; metal avg `0.0072` n `20`; unknown avg `1.2136` n `828`
- 1h: commodity avg `0.0276` n `12`; crypto_alt avg `-0.0382` n `233`; crypto_major avg `-0.1878` n `8`; equity avg `-0.0014` n `136`; fx avg `0.0011` n `6`; index avg `0.0008` n `26`; metal avg `-0.0097` n `20`; unknown avg `2.5743` n `828`
- 4h: commodity avg `-0.1032` n `12`; crypto_alt avg `-0.2459` n `233`; crypto_major avg `-0.255` n `8`; equity avg `-0.0586` n `136`; fx avg `-0.0311` n `6`; index avg `0.0034` n `26`; metal avg `0.0194` n `20`; unknown avg `1.0124` n `770`
- 24h: commodity avg `-0.7291` n `12`; crypto_alt avg `0.3965` n `233`; crypto_major avg `1.2135` n `8`; equity avg `0.8869` n `136`; fx avg `-0.2005` n `6`; index avg `0.3304` n `26`; metal avg `0.2805` n `20`; unknown avg `1.7001` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
