# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T01:22:26.615187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `-0.1821` n `239`; crypto_major avg `-0.1383` n `8`; equity avg `-0.336` n `163`; fx avg `0.0272` n `6`; index avg `-0.0439` n `27`; metal avg `-0.0645` n `20`; unknown avg `6.3417` n `1264`
- 1h: commodity avg `-0.0336` n `13`; crypto_alt avg `-0.5422` n `239`; crypto_major avg `-0.5115` n `8`; equity avg `-0.528` n `163`; fx avg `-0.0134` n `6`; index avg `-0.07` n `27`; metal avg `-0.1938` n `20`; unknown avg `3.0376` n `1264`
- 4h: commodity avg `-0.0165` n `13`; crypto_alt avg `0.2453` n `239`; crypto_major avg `0.5085` n `8`; equity avg `1.3394` n `163`; fx avg `-0.0528` n `6`; index avg `0.0673` n `27`; metal avg `-0.2313` n `20`; unknown avg `3.5454` n `1211`
- 24h: commodity avg `0.2533` n `13`; crypto_alt avg `0.9712` n `239`; crypto_major avg `1.012` n `8`; equity avg `0.6499` n `163`; fx avg `-0.0916` n `6`; index avg `-0.0203` n `27`; metal avg `-0.2794` n `20`; unknown avg `7.2447` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
