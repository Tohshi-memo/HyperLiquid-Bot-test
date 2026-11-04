# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T21:07:33.249382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `13`; crypto_alt avg `0.2232` n `239`; crypto_major avg `0.2224` n `8`; equity avg `0.1344` n `158`; fx avg `0.0046` n `6`; index avg `0.0429` n `27`; metal avg `0.0474` n `20`; unknown avg `0.2266` n `1234`
- 1h: commodity avg `-0.0177` n `13`; crypto_alt avg `0.3535` n `239`; crypto_major avg `0.1567` n `8`; equity avg `0.1053` n `158`; fx avg `0.0026` n `6`; index avg `0.0288` n `27`; metal avg `0.0007` n `20`; unknown avg `0.3344` n `1216`
- 4h: commodity avg `0.1119` n `13`; crypto_alt avg `-0.9683` n `239`; crypto_major avg `-0.665` n `8`; equity avg `-0.38` n `158`; fx avg `0.0164` n `6`; index avg `-0.0418` n `27`; metal avg `0.0327` n `20`; unknown avg `19.6415` n `1194`
- 24h: commodity avg `-1.7807` n `13`; crypto_alt avg `1.3967` n `239`; crypto_major avg `1.6535` n `8`; equity avg `-1.1575` n `158`; fx avg `0.0625` n `6`; index avg `0.1249` n `27`; metal avg `1.319` n `20`; unknown avg `-0.057` n `1079`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2662`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
