# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T09:22:28.543344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.136` n `13`; crypto_alt avg `-0.2268` n `239`; crypto_major avg `-0.4078` n `8`; equity avg `-0.122` n `158`; fx avg `-0.0128` n `6`; index avg `-0.0476` n `27`; metal avg `-0.0413` n `20`; unknown avg `0.2753` n `1263`
- 1h: commodity avg `0.227` n `13`; crypto_alt avg `0.6457` n `239`; crypto_major avg `0.2869` n `8`; equity avg `0.3404` n `158`; fx avg `0.0272` n `6`; index avg `0.0334` n `27`; metal avg `0.0404` n `20`; unknown avg `156.6024` n `1233`
- 4h: commodity avg `-0.0768` n `13`; crypto_alt avg `-0.083` n `239`; crypto_major avg `-0.6329` n `8`; equity avg `-0.6979` n `158`; fx avg `0.0216` n `6`; index avg `-0.1152` n `27`; metal avg `-0.2303` n `20`; unknown avg `173.9517` n `1109`
- 24h: commodity avg `-0.039` n `13`; crypto_alt avg `-1.7617` n `239`; crypto_major avg `-3.103` n `8`; equity avg `-0.6204` n `158`; fx avg `-0.0961` n `6`; index avg `-0.0701` n `27`; metal avg `0.2371` n `20`; unknown avg `0.5405` n `948`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
