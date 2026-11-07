# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T22:37:32.508290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `13`; crypto_alt avg `0.118` n `239`; crypto_major avg `-0.0005` n `8`; equity avg `-0.0201` n `158`; fx avg `-0.0053` n `6`; index avg `-0.0002` n `27`; metal avg `0.0049` n `20`; unknown avg `0.7485` n `1262`
- 1h: commodity avg `0.0361` n `13`; crypto_alt avg `0.6089` n `239`; crypto_major avg `0.3423` n `8`; equity avg `0.0248` n `158`; fx avg `-0.0027` n `6`; index avg `-0.0017` n `27`; metal avg `0.0078` n `20`; unknown avg `0.3728` n `1250`
- 4h: commodity avg `0.0811` n `13`; crypto_alt avg `-0.4814` n `239`; crypto_major avg `-0.2552` n `8`; equity avg `-0.2567` n `158`; fx avg `0.0013` n `6`; index avg `-0.0253` n `27`; metal avg `-0.0069` n `20`; unknown avg `0.4319` n `1214`
- 24h: commodity avg `0.0767` n `13`; crypto_alt avg `-1.4872` n `239`; crypto_major avg `-0.836` n `8`; equity avg `-0.2614` n `158`; fx avg `-0.0167` n `6`; index avg `0.0467` n `27`; metal avg `-0.0235` n `20`; unknown avg `146.3212` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
