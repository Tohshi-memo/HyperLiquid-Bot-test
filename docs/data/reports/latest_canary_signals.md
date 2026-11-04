# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T13:22:28.782283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `13`; crypto_alt avg `-0.0339` n `239`; crypto_major avg `0.0364` n `8`; equity avg `0.1128` n `158`; fx avg `-0.0004` n `6`; index avg `0.026` n `27`; metal avg `-0.0138` n `20`; unknown avg `0.0869` n `1264`
- 1h: commodity avg `-0.0161` n `13`; crypto_alt avg `-0.0958` n `239`; crypto_major avg `0.0` n `8`; equity avg `-0.6428` n `158`; fx avg `0.0109` n `6`; index avg `-0.0225` n `27`; metal avg `-0.0693` n `20`; unknown avg `-0.0625` n `1258`
- 4h: commodity avg `-0.2356` n `13`; crypto_alt avg `-0.429` n `239`; crypto_major avg `-0.2684` n `8`; equity avg `-1.0818` n `158`; fx avg `0.011` n `6`; index avg `0.0168` n `27`; metal avg `-0.0402` n `20`; unknown avg `1.4362` n `1254`
- 24h: commodity avg `-0.447` n `13`; crypto_alt avg `0.9261` n `239`; crypto_major avg `0.47` n `8`; equity avg `0.3613` n `158`; fx avg `0.1626` n `6`; index avg `0.1285` n `27`; metal avg `0.8029` n `20`; unknown avg `21.8385` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2513`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
