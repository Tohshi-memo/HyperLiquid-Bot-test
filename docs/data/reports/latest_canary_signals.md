# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T21:52:28.516040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0426` n `13`; crypto_alt avg `0.0761` n `239`; crypto_major avg `-0.0495` n `8`; equity avg `-0.0026` n `158`; fx avg `0.0059` n `6`; index avg `-0.0089` n `27`; metal avg `-0.0043` n `20`; unknown avg `1.7382` n `1264`
- 1h: commodity avg `-0.134` n `13`; crypto_alt avg `0.3547` n `239`; crypto_major avg `0.0735` n `8`; equity avg `0.5384` n `158`; fx avg `0.0009` n `6`; index avg `0.086` n `27`; metal avg `0.0077` n `20`; unknown avg `0.285` n `1232`
- 4h: commodity avg `-0.0584` n `13`; crypto_alt avg `-0.2856` n `239`; crypto_major avg `-0.4924` n `8`; equity avg `-0.2449` n `158`; fx avg `0.0159` n `6`; index avg `-0.02` n `27`; metal avg `-0.024` n `20`; unknown avg `-0.145` n `1190`
- 24h: commodity avg `-1.8824` n `13`; crypto_alt avg `1.2436` n `239`; crypto_major avg `1.3972` n `8`; equity avg `-1.5056` n `158`; fx avg `0.053` n `6`; index avg `0.0836` n `27`; metal avg `1.2362` n `20`; unknown avg `0.0283` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2662`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
