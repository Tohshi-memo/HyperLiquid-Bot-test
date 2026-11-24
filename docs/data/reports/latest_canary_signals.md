# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T12:07:28.820047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.5029` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0814` n `13`; crypto_alt avg `-0.09` n `239`; crypto_major avg `-0.0538` n `8`; equity avg `-0.1257` n `166`; fx avg `-0.015` n `6`; index avg `-0.0244` n `27`; metal avg `-0.0686` n `20`; unknown avg `0.3192` n `1250`
- 1h: commodity avg `0.1207` n `13`; crypto_alt avg `0.0481` n `239`; crypto_major avg `0.5667` n `8`; equity avg `0.3967` n `166`; fx avg `0.0272` n `6`; index avg `0.0216` n `27`; metal avg `0.0543` n `20`; unknown avg `0.5932` n `1256`
- 4h: commodity avg `0.1401` n `13`; crypto_alt avg `-1.4338` n `239`; crypto_major avg `-0.3519` n `8`; equity avg `-1.8548` n `166`; fx avg `0.108` n `6`; index avg `-0.2465` n `27`; metal avg `-0.0795` n `20`; unknown avg `500.3989` n `1200`
- 24h: commodity avg `-0.3192` n `13`; crypto_alt avg `-1.4866` n `239`; crypto_major avg `-1.1811` n `8`; equity avg `1.4231` n `166`; fx avg `-0.0577` n `6`; index avg `0.2806` n `27`; metal avg `-0.3412` n `20`; unknown avg `0.2326` n `1132`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
