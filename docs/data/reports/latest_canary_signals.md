# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T22:07:34.380598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0557` n `13`; crypto_alt avg `-0.2981` n `239`; crypto_major avg `-0.1008` n `8`; equity avg `-0.2579` n `158`; fx avg `0.0098` n `6`; index avg `-0.0204` n `27`; metal avg `-0.0099` n `20`; unknown avg `-0.0598` n `1250`
- 1h: commodity avg `0.1654` n `13`; crypto_alt avg `-0.4782` n `239`; crypto_major avg `-0.297` n `8`; equity avg `0.0396` n `158`; fx avg `0.0101` n `6`; index avg `-0.0617` n `27`; metal avg `-0.0207` n `20`; unknown avg `0.4802` n `1252`
- 4h: commodity avg `0.2178` n `13`; crypto_alt avg `0.8282` n `239`; crypto_major avg `0.0243` n `8`; equity avg `0.0493` n `158`; fx avg `-0.0154` n `6`; index avg `-0.2278` n `27`; metal avg `-0.1816` n `20`; unknown avg `3.8032` n `1194`
- 24h: commodity avg `0.9941` n `13`; crypto_alt avg `-5.2114` n `239`; crypto_major avg `-5.4078` n `8`; equity avg `-8.7377` n `158`; fx avg `0.1069` n `6`; index avg `-1.3095` n `27`; metal avg `0.0425` n `20`; unknown avg `228.6863` n `1062`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
