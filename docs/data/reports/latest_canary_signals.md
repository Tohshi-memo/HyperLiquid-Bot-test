# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T21:23:19.969573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.81` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0099` n `13`; crypto_alt avg `0.2728` n `239`; crypto_major avg `0.6117` n `8`; equity avg `0.3573` n `166`; fx avg `0.0057` n `6`; index avg `0.0131` n `27`; metal avg `0.003` n `20`; unknown avg `-0.3198` n `1260`
- 1h: commodity avg `0.1117` n `13`; crypto_alt avg `-0.1363` n `239`; crypto_major avg `-0.1775` n `8`; equity avg `0.2977` n `166`; fx avg `-0.004` n `6`; index avg `0.0041` n `27`; metal avg `-0.0472` n `20`; unknown avg `3.3061` n `1230`
- 4h: commodity avg `0.4723` n `13`; crypto_alt avg `-0.0579` n `239`; crypto_major avg `-0.8759` n `8`; equity avg `-0.5658` n `166`; fx avg `-0.0418` n `6`; index avg `-0.1642` n `27`; metal avg `-0.0468` n `20`; unknown avg `241.5924` n `1220`
- 24h: commodity avg `0.2722` n `13`; crypto_alt avg `-5.6583` n `239`; crypto_major avg `-6.1422` n `8`; equity avg `-6.6958` n `166`; fx avg `0.0026` n `6`; index avg `-0.7481` n `27`; metal avg `-1.0813` n `20`; unknown avg `28.781` n `1137`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
