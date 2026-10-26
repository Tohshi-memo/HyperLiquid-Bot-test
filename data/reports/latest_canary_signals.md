# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T07:07:36.707043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0308` n `13`; crypto_alt avg `-0.0102` n `237`; crypto_major avg `0.0963` n `8`; equity avg `0.0883` n `152`; fx avg `-0.0102` n `6`; index avg `0.03` n `26`; metal avg `-0.0105` n `20`; unknown avg `0.7694` n `1236`
- 1h: commodity avg `0.0838` n `13`; crypto_alt avg `-0.15` n `237`; crypto_major avg `-0.0481` n `8`; equity avg `-0.1554` n `152`; fx avg `-0.0161` n `6`; index avg `-0.0386` n `26`; metal avg `-0.0572` n `20`; unknown avg `0.6595` n `1238`
- 4h: commodity avg `0.0719` n `13`; crypto_alt avg `-0.1017` n `237`; crypto_major avg `0.284` n `8`; equity avg `-0.0254` n `152`; fx avg `0.0149` n `6`; index avg `-0.0518` n `26`; metal avg `-0.0993` n `20`; unknown avg `0.5996` n `1200`
- 24h: commodity avg `-0.6346` n `13`; crypto_alt avg `-0.6615` n `237`; crypto_major avg `-0.3778` n `8`; equity avg `-0.4844` n `152`; fx avg `0.0479` n `6`; index avg `-0.0326` n `26`; metal avg `0.0939` n `20`; unknown avg `-0.5323` n `983`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2527`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
