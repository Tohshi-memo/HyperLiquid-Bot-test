# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T16:37:31.001622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2408` n `12`; crypto_alt avg `0.4533` n `230`; crypto_major avg `0.5175` n `8`; equity avg `0.6132` n `102`; fx avg `-0.0082` n `6`; index avg `0.085` n `25`; metal avg `0.0795` n `20`; unknown avg `0.7052` n `774`
- 1h: commodity avg `-0.1251` n `12`; crypto_alt avg `0.5917` n `230`; crypto_major avg `0.6794` n `8`; equity avg `0.9788` n `102`; fx avg `-0.0123` n `6`; index avg `0.1286` n `25`; metal avg `0.1677` n `20`; unknown avg `0.5761` n `774`
- 4h: commodity avg `-0.2498` n `12`; crypto_alt avg `-1.0912` n `230`; crypto_major avg `-0.6646` n `8`; equity avg `-2.0096` n `102`; fx avg `-0.0634` n `6`; index avg `-0.4826` n `25`; metal avg `0.1158` n `20`; unknown avg `-0.1202` n `774`
- 24h: commodity avg `-0.7014` n `12`; crypto_alt avg `-1.2864` n `230`; crypto_major avg `-0.4899` n `8`; equity avg `-1.4232` n `102`; fx avg `0.0267` n `6`; index avg `-0.433` n `25`; metal avg `0.3369` n `20`; unknown avg `-0.259` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1998`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
