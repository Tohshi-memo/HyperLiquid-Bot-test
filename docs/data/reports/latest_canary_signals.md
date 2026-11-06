# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T11:52:33.577929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0617` n `13`; crypto_alt avg `-0.008` n `239`; crypto_major avg `0.1224` n `8`; equity avg `0.2468` n `158`; fx avg `-0.0024` n `6`; index avg `0.0211` n `27`; metal avg `0.0013` n `20`; unknown avg `-0.0816` n `1219`
- 1h: commodity avg `-0.0549` n `13`; crypto_alt avg `0.3487` n `239`; crypto_major avg `0.2957` n `8`; equity avg `0.809` n `158`; fx avg `0.0305` n `6`; index avg `0.0434` n `27`; metal avg `0.1134` n `20`; unknown avg `30.2402` n `1207`
- 4h: commodity avg `-0.1827` n `13`; crypto_alt avg `1.2745` n `239`; crypto_major avg `1.0449` n `8`; equity avg `2.0854` n `158`; fx avg `0.0476` n `6`; index avg `0.236` n `27`; metal avg `0.1899` n `20`; unknown avg `23.2707` n `1146`
- 24h: commodity avg `0.6332` n `13`; crypto_alt avg `-2.8569` n `239`; crypto_major avg `-5.0702` n `8`; equity avg `-4.1298` n `158`; fx avg `0.0192` n `6`; index avg `-0.5921` n `27`; metal avg `-0.3515` n `20`; unknown avg `14.9964` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
