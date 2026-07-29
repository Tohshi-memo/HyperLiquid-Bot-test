# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T07:07:24.221524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.0116` n `230`; crypto_major avg `-0.0032` n `8`; equity avg `0.0164` n `102`; fx avg `0.0085` n `6`; index avg `0.0257` n `25`; metal avg `0.0123` n `20`; unknown avg `-0.0347` n `777`
- 1h: commodity avg `-0.0937` n `12`; crypto_alt avg `0.2152` n `230`; crypto_major avg `0.438` n `8`; equity avg `0.8925` n `102`; fx avg `-0.0067` n `6`; index avg `0.3566` n `25`; metal avg `0.0777` n `20`; unknown avg `-0.0848` n `777`
- 4h: commodity avg `-0.0997` n `12`; crypto_alt avg `-0.4769` n `230`; crypto_major avg `0.5443` n `8`; equity avg `0.5977` n `102`; fx avg `-0.0535` n `6`; index avg `0.2552` n `25`; metal avg `0.11` n `20`; unknown avg `-0.1171` n `761`
- 24h: commodity avg `-0.0269` n `12`; crypto_alt avg `-1.5176` n `230`; crypto_major avg `1.0427` n `8`; equity avg `-1.3416` n `102`; fx avg `-0.1242` n `6`; index avg `-0.1593` n `25`; metal avg `0.0121` n `20`; unknown avg `-0.3221` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
