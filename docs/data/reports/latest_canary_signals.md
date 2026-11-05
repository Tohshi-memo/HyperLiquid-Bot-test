# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T12:22:34.166722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `13`; crypto_alt avg `-0.1458` n `239`; crypto_major avg `-0.1271` n `8`; equity avg `-0.2544` n `158`; fx avg `0.0234` n `6`; index avg `-0.0341` n `27`; metal avg `-0.0225` n `20`; unknown avg `0.0635` n `1255`
- 1h: commodity avg `0.1625` n `13`; crypto_alt avg `-0.656` n `239`; crypto_major avg `-0.4482` n `8`; equity avg `-0.5302` n `158`; fx avg `0.0447` n `6`; index avg `-0.0509` n `27`; metal avg `-0.0655` n `20`; unknown avg `0.215` n `1245`
- 4h: commodity avg `0.3953` n `13`; crypto_alt avg `-0.8141` n `239`; crypto_major avg `-0.5737` n `8`; equity avg `-0.6027` n `158`; fx avg `0.0491` n `6`; index avg `-0.0594` n `27`; metal avg `0.08` n `20`; unknown avg `37.107` n `1145`
- 24h: commodity avg `-1.039` n `13`; crypto_alt avg `0.3851` n `239`; crypto_major avg `1.6559` n `8`; equity avg `-2.6199` n `158`; fx avg `0.008` n `6`; index avg `-0.2623` n `27`; metal avg `0.6569` n `20`; unknown avg `39.8794` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2388`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2031`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
