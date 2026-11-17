# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T21:22:24.616525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `13`; crypto_alt avg `0.2758` n `239`; crypto_major avg `0.3396` n `8`; equity avg `0.4361` n `163`; fx avg `-0.0101` n `6`; index avg `0.0493` n `27`; metal avg `0.0384` n `20`; unknown avg `4.998` n `1263`
- 1h: commodity avg `0.0581` n `13`; crypto_alt avg `0.513` n `239`; crypto_major avg `0.4704` n `8`; equity avg `0.911` n `163`; fx avg `-0.0132` n `6`; index avg `0.1228` n `27`; metal avg `0.0434` n `20`; unknown avg `3.0245` n `1247`
- 4h: commodity avg `-0.0436` n `13`; crypto_alt avg `0.6436` n `239`; crypto_major avg `0.7947` n `8`; equity avg `0.667` n `163`; fx avg `-0.0326` n `6`; index avg `0.0605` n `27`; metal avg `-0.144` n `20`; unknown avg `3.4793` n `1239`
- 24h: commodity avg `0.1917` n `13`; crypto_alt avg `0.3369` n `239`; crypto_major avg `0.3353` n `8`; equity avg `-0.539` n `163`; fx avg `0.0306` n `6`; index avg `-0.0602` n `27`; metal avg `-0.007` n `20`; unknown avg `7.9599` n `1107`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
