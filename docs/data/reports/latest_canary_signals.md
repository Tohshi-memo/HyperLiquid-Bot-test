# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T09:58:58.354327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `0.1237` n `230`; crypto_major avg `0.1344` n `8`; equity avg `0.1513` n `100`; fx avg `-0.0107` n `6`; index avg `0.0071` n `25`; metal avg `0.0665` n `20`; unknown avg `0.0175` n `773`
- 1h: commodity avg `-0.0837` n `12`; crypto_alt avg `-0.017` n `230`; crypto_major avg `-0.1517` n `8`; equity avg `0.3585` n `100`; fx avg `-0.0198` n `6`; index avg `0.0443` n `25`; metal avg `0.1046` n `20`; unknown avg `0.1283` n `773`
- 4h: commodity avg `-0.4722` n `12`; crypto_alt avg `0.1758` n `230`; crypto_major avg `0.2286` n `8`; equity avg `0.6343` n `100`; fx avg `-0.0385` n `6`; index avg `0.103` n `25`; metal avg `0.3695` n `20`; unknown avg `0.2189` n `756`
- 24h: commodity avg `-0.3126` n `12`; crypto_alt avg `-0.9868` n `230`; crypto_major avg `-1.4471` n `8`; equity avg `-1.5445` n `99`; fx avg `-0.1508` n `6`; index avg `-0.4183` n `25`; metal avg `-0.2902` n `20`; unknown avg `0.2183` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0971`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0857`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0805`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
