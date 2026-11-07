# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T22:22:27.313416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `13`; crypto_alt avg `0.1907` n `239`; crypto_major avg `0.1478` n `8`; equity avg `0.0178` n `158`; fx avg `-0.0014` n `6`; index avg `-0.0025` n `27`; metal avg `0.0005` n `20`; unknown avg `0.6616` n `1262`
- 1h: commodity avg `0.0218` n `13`; crypto_alt avg `0.4337` n `239`; crypto_major avg `0.3569` n `8`; equity avg `0.0704` n `158`; fx avg `0.0058` n `6`; index avg `0.0079` n `27`; metal avg `0.0066` n `20`; unknown avg `-0.1929` n `1250`
- 4h: commodity avg `0.0756` n `13`; crypto_alt avg `-0.7393` n `239`; crypto_major avg `-0.3441` n `8`; equity avg `-0.2665` n `158`; fx avg `0.0077` n `6`; index avg `-0.0254` n `27`; metal avg `-0.0123` n `20`; unknown avg `-0.024` n `1214`
- 24h: commodity avg `0.0676` n `13`; crypto_alt avg `-1.6279` n `239`; crypto_major avg `-0.8102` n `8`; equity avg `-0.2343` n `158`; fx avg `-0.0129` n `6`; index avg `0.0252` n `27`; metal avg `-0.0397` n `20`; unknown avg `146.3925` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
