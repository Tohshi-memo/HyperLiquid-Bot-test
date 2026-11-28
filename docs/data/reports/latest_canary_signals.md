# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T20:37:24.063872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `13`; crypto_alt avg `-0.2301` n `239`; crypto_major avg `-0.0895` n `8`; equity avg `-0.0382` n `168`; fx avg `0.0` n `6`; index avg `-0.0044` n `27`; metal avg `-0.0058` n `20`; unknown avg `0.0602` n `1252`
- 1h: commodity avg `0.0134` n `13`; crypto_alt avg `0.0024` n `239`; crypto_major avg `0.0106` n `8`; equity avg `0.042` n `168`; fx avg `-0.0091` n `6`; index avg `0.0028` n `27`; metal avg `0.0052` n `20`; unknown avg `1.5419` n `1230`
- 4h: commodity avg `0.1128` n `13`; crypto_alt avg `-0.189` n `239`; crypto_major avg `-0.0487` n `8`; equity avg `0.2012` n `168`; fx avg `-0.0215` n `6`; index avg `0.0168` n `27`; metal avg `0.0254` n `20`; unknown avg `55.3468` n `1189`
- 24h: commodity avg `-0.0011` n `13`; crypto_alt avg `-3.4126` n `239`; crypto_major avg `-1.4004` n `8`; equity avg `-0.1356` n `168`; fx avg `-0.0145` n `6`; index avg `-0.0277` n `27`; metal avg `0.0507` n `20`; unknown avg `-0.4494` n `1043`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
