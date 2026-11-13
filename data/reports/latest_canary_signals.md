# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T00:22:32.577966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `13`; crypto_alt avg `-0.0388` n `239`; crypto_major avg `-0.0233` n `8`; equity avg `-0.0308` n `162`; fx avg `-0.0056` n `6`; index avg `0.0027` n `27`; metal avg `-0.022` n `20`; unknown avg `0.4065` n `1259`
- 1h: commodity avg `-0.07` n `13`; crypto_alt avg `0.1338` n `239`; crypto_major avg `0.2525` n `8`; equity avg `0.5832` n `162`; fx avg `0.0036` n `6`; index avg `0.0639` n `27`; metal avg `0.0716` n `20`; unknown avg `0.7734` n `1253`
- 4h: commodity avg `-0.0243` n `13`; crypto_alt avg `0.6152` n `239`; crypto_major avg `0.4044` n `8`; equity avg `1.2027` n `162`; fx avg `0.0017` n `6`; index avg `0.1241` n `27`; metal avg `0.0361` n `20`; unknown avg `193.1016` n `1193`
- 24h: commodity avg `0.8413` n `13`; crypto_alt avg `-1.046` n `239`; crypto_major avg `-1.7659` n `8`; equity avg `0.0444` n `162`; fx avg `-0.0477` n `6`; index avg `0.1163` n `27`; metal avg `-0.5358` n `20`; unknown avg `51.365` n `1121`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
