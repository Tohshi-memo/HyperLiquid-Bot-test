# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T20:22:27.523690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `13`; crypto_alt avg `0.0284` n `239`; crypto_major avg `0.0353` n `8`; equity avg `-0.0385` n `158`; fx avg `0.0024` n `6`; index avg `-0.004` n `27`; metal avg `-0.0072` n `20`; unknown avg `1.2695` n `1262`
- 1h: commodity avg `0.013` n `13`; crypto_alt avg `-0.1648` n `239`; crypto_major avg `-0.0656` n `8`; equity avg `-0.3062` n `158`; fx avg `0.0015` n `6`; index avg `-0.0428` n `27`; metal avg `-0.0124` n `20`; unknown avg `3.6636` n `1234`
- 4h: commodity avg `-0.1373` n `13`; crypto_alt avg `-0.3218` n `239`; crypto_major avg `-0.288` n `8`; equity avg `0.0716` n `158`; fx avg `-0.0055` n `6`; index avg `0.0139` n `27`; metal avg `0.0164` n `20`; unknown avg `0.9646` n `1186`
- 24h: commodity avg `-0.0919` n `13`; crypto_alt avg `-1.6238` n `239`; crypto_major avg `-0.2416` n `8`; equity avg `0.1904` n `158`; fx avg `0.0447` n `6`; index avg `-0.0135` n `27`; metal avg `-0.0218` n `20`; unknown avg `-0.1623` n `1032`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
