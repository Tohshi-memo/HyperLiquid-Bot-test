# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T00:22:23.234749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `13`; crypto_alt avg `0.1603` n `239`; crypto_major avg `0.0774` n `8`; equity avg `-0.1602` n `168`; fx avg `-0.032` n `6`; index avg `-0.0407` n `27`; metal avg `0.0041` n `20`; unknown avg `0.5872` n `1261`
- 1h: commodity avg `0.0266` n `13`; crypto_alt avg `0.4308` n `239`; crypto_major avg `0.3197` n `8`; equity avg `0.0734` n `168`; fx avg `0.0031` n `6`; index avg `-0.0015` n `27`; metal avg `0.0359` n `20`; unknown avg `1.8516` n `1247`
- 4h: commodity avg `0.0613` n `13`; crypto_alt avg `-0.1026` n `239`; crypto_major avg `-0.3229` n `8`; equity avg `-0.2421` n `168`; fx avg `0.0084` n `6`; index avg `-0.0177` n `27`; metal avg `-0.0183` n `20`; unknown avg `67.957` n `1143`
- 24h: commodity avg `0.1462` n `13`; crypto_alt avg `0.5321` n `239`; crypto_major avg `-0.1685` n `8`; equity avg `-0.4036` n `168`; fx avg `0.029` n `6`; index avg `-0.0526` n `27`; metal avg `-0.0094` n `20`; unknown avg `210.4383` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
