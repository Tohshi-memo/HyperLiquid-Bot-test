# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T05:52:26.762362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `0.6758` n `239`; crypto_major avg `0.4338` n `8`; equity avg `0.4869` n `158`; fx avg `0.0168` n `6`; index avg `0.0458` n `27`; metal avg `0.2199` n `20`; unknown avg `76.7911` n `1264`
- 1h: commodity avg `0.2121` n `13`; crypto_alt avg `1.3949` n `239`; crypto_major avg `1.0525` n `8`; equity avg `1.6201` n `158`; fx avg `0.0058` n `6`; index avg `0.2534` n `27`; metal avg `0.5875` n `20`; unknown avg `3.6283` n `1258`
- 4h: commodity avg `0.0552` n `13`; crypto_alt avg `1.946` n `239`; crypto_major avg `1.4984` n `8`; equity avg `1.493` n `158`; fx avg `0.0536` n `6`; index avg `0.2579` n `27`; metal avg `0.5318` n `20`; unknown avg `1.7992` n `1254`
- 24h: commodity avg `-0.0949` n `13`; crypto_alt avg `2.1916` n `239`; crypto_major avg `1.441` n `8`; equity avg `1.8817` n `158`; fx avg `0.1205` n `6`; index avg `0.0716` n `27`; metal avg `0.5171` n `20`; unknown avg `190.5184` n `1051`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
