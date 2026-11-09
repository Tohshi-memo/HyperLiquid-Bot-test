# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T03:07:26.903825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0646` n `13`; crypto_alt avg `-0.2645` n `239`; crypto_major avg `-0.3058` n `8`; equity avg `-0.1164` n `158`; fx avg `0.0204` n `6`; index avg `-0.0073` n `27`; metal avg `-0.0468` n `20`; unknown avg `-0.0989` n `1258`
- 1h: commodity avg `0.1703` n `13`; crypto_alt avg `-0.1931` n `239`; crypto_major avg `-0.3235` n `8`; equity avg `0.1414` n `158`; fx avg `-0.0172` n `6`; index avg `0.0101` n `27`; metal avg `-0.1254` n `20`; unknown avg `-0.472` n `1254`
- 4h: commodity avg `0.1615` n `13`; crypto_alt avg `0.6197` n `239`; crypto_major avg `-0.3528` n `8`; equity avg `1.0816` n `158`; fx avg `-0.0798` n `6`; index avg `0.1282` n `27`; metal avg `0.3969` n `20`; unknown avg `2.4952` n `1236`
- 24h: commodity avg `0.1184` n `13`; crypto_alt avg `-1.816` n `239`; crypto_major avg `-2.3318` n `8`; equity avg `0.6272` n `158`; fx avg `-0.0719` n `6`; index avg `0.0765` n `27`; metal avg `0.4495` n `20`; unknown avg `1.1942` n `992`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
