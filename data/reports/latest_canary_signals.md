# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T00:22:31.989200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `13`; crypto_alt avg `-0.0032` n `239`; crypto_major avg `0.0645` n `8`; equity avg `0.0094` n `166`; fx avg `-0.0107` n `6`; index avg `0.0119` n `27`; metal avg `-0.0082` n `20`; unknown avg `-0.0941` n `1259`
- 1h: commodity avg `-0.0204` n `13`; crypto_alt avg `0.0564` n `239`; crypto_major avg `0.1587` n `8`; equity avg `0.0965` n `166`; fx avg `-0.0102` n `6`; index avg `0.0194` n `27`; metal avg `0.0116` n `20`; unknown avg `176.152` n `1252`
- 4h: commodity avg `-0.0308` n `13`; crypto_alt avg `0.079` n `239`; crypto_major avg `-0.0957` n `8`; equity avg `0.1749` n `166`; fx avg `-0.0016` n `6`; index avg `0.0538` n `27`; metal avg `-0.0556` n `20`; unknown avg `-0.153` n `1202`
- 24h: commodity avg `0.0177` n `13`; crypto_alt avg `0.4722` n `239`; crypto_major avg `1.9853` n `8`; equity avg `0.8323` n `166`; fx avg `-0.0355` n `6`; index avg `0.1859` n `27`; metal avg `0.118` n `20`; unknown avg `232.5582` n `1082`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
