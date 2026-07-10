# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T05:07:34.940336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0705` n `12`; crypto_alt avg `-0.0075` n `229`; crypto_major avg `-0.1031` n `8`; equity avg `-0.108` n `91`; fx avg `-0.0178` n `6`; index avg `-0.0258` n `25`; metal avg `0.0041` n `20`; unknown avg `0.0719` n `765`
- 1h: commodity avg `-0.0118` n `12`; crypto_alt avg `-0.0116` n `229`; crypto_major avg `-0.0519` n `8`; equity avg `-0.2317` n `91`; fx avg `0.0135` n `6`; index avg `-0.0684` n `25`; metal avg `-0.0265` n `20`; unknown avg `-0.0512` n `765`
- 4h: commodity avg `0.078` n `12`; crypto_alt avg `0.8792` n `229`; crypto_major avg `1.209` n `8`; equity avg `0.1603` n `91`; fx avg `0.0134` n `6`; index avg `0.0464` n `25`; metal avg `0.1155` n `20`; unknown avg `2.3907` n `763`
- 24h: commodity avg `-0.993` n `12`; crypto_alt avg `1.3478` n `229`; crypto_major avg `1.5123` n `8`; equity avg `1.5339` n `91`; fx avg `0.0574` n `6`; index avg `0.3842` n `25`; metal avg `0.9174` n `20`; unknown avg `0.1726` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
