# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T21:07:34.238494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `0.0781` n `239`; crypto_major avg `0.074` n `8`; equity avg `0.0394` n `168`; fx avg `0.0085` n `6`; index avg `-0.0354` n `27`; metal avg `0.0214` n `20`; unknown avg `0.1104` n `1205`
- 1h: commodity avg `0.0004` n `13`; crypto_alt avg `0.155` n `239`; crypto_major avg `0.0672` n `8`; equity avg `0.1354` n `168`; fx avg `0.008` n `6`; index avg `0.0241` n `27`; metal avg `0.0492` n `20`; unknown avg `0.8487` n `1213`
- 4h: commodity avg `0.0206` n `13`; crypto_alt avg `0.2875` n `239`; crypto_major avg `0.0475` n `8`; equity avg `0.7179` n `168`; fx avg `-0.0026` n `6`; index avg `0.0773` n `27`; metal avg `0.2535` n `20`; unknown avg `168.6699` n `1186`
- 24h: commodity avg `-0.4804` n `13`; crypto_alt avg `0.0013` n `239`; crypto_major avg `-0.1328` n `8`; equity avg `3.1879` n `168`; fx avg `-0.1506` n `6`; index avg `0.3147` n `27`; metal avg `0.9556` n `20`; unknown avg `266.1517` n `1019`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
