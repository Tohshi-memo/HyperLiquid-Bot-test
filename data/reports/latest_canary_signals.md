# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T11:22:35.347551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.023` n `13`; crypto_alt avg `0.1816` n `239`; crypto_major avg `0.1253` n `8`; equity avg `0.0976` n `158`; fx avg `-0.0029` n `6`; index avg `0.0076` n `27`; metal avg `0.0687` n `20`; unknown avg `0.2199` n `1255`
- 1h: commodity avg `0.0116` n `13`; crypto_alt avg `-0.1637` n `239`; crypto_major avg `-0.0829` n `8`; equity avg `-0.1567` n `158`; fx avg `0.0062` n `6`; index avg `-0.0102` n `27`; metal avg `0.1324` n `20`; unknown avg `18.9102` n `1237`
- 4h: commodity avg `0.2864` n `13`; crypto_alt avg `0.0911` n `239`; crypto_major avg `0.1113` n `8`; equity avg `0.0256` n `158`; fx avg `-0.0133` n `6`; index avg `0.0476` n `27`; metal avg `0.1768` n `20`; unknown avg `21.6114` n `1133`
- 24h: commodity avg `-1.3125` n `13`; crypto_alt avg `0.0953` n `239`; crypto_major avg `1.3069` n `8`; equity avg `-3.4561` n `158`; fx avg `-0.0192` n `6`; index avg `-0.2806` n `27`; metal avg `0.6885` n `20`; unknown avg `22.4981` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2431`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
