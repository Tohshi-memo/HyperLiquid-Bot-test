# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T21:22:31.973485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0455` n `13`; crypto_alt avg `-0.0288` n `239`; crypto_major avg `-0.0937` n `8`; equity avg `0.3524` n `158`; fx avg `-0.0016` n `6`; index avg `0.0153` n `27`; metal avg `0.0221` n `20`; unknown avg `0.274` n `1264`
- 1h: commodity avg `-0.0905` n `13`; crypto_alt avg `-0.0627` n `239`; crypto_major avg `-0.1812` n `8`; equity avg `0.3653` n `158`; fx avg `-0.0063` n `6`; index avg `0.0227` n `27`; metal avg `0.0099` n `20`; unknown avg `-0.0622` n `1216`
- 4h: commodity avg `0.1627` n `13`; crypto_alt avg `-0.4968` n `239`; crypto_major avg `-0.5439` n `8`; equity avg `-0.2444` n `158`; fx avg `0.0108` n `6`; index avg `-0.0432` n `27`; metal avg `0.0773` n `20`; unknown avg `19.7263` n `1194`
- 24h: commodity avg `-1.848` n `13`; crypto_alt avg `1.1618` n `239`; crypto_major avg `1.4088` n `8`; equity avg `-1.4381` n `158`; fx avg `0.0527` n `6`; index avg `0.0729` n `27`; metal avg `1.3112` n `20`; unknown avg `0.2139` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2662`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
