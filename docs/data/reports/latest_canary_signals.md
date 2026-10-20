# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T04:07:25.515474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0262` n `13`; crypto_alt avg `-0.0503` n `237`; crypto_major avg `-0.0101` n `8`; equity avg `-0.2296` n `151`; fx avg `0.0018` n `6`; index avg `-0.0614` n `26`; metal avg `-0.0078` n `20`; unknown avg `0.4005` n `1190`
- 1h: commodity avg `-0.0333` n `13`; crypto_alt avg `0.255` n `237`; crypto_major avg `0.1472` n `8`; equity avg `-0.5104` n `151`; fx avg `-0.0059` n `6`; index avg `-0.1351` n `26`; metal avg `-0.0048` n `20`; unknown avg `9.4185` n `1190`
- 4h: commodity avg `0.1063` n `13`; crypto_alt avg `0.6038` n `237`; crypto_major avg `0.2566` n `8`; equity avg `-0.1748` n `151`; fx avg `0.0368` n `6`; index avg `-0.1087` n `26`; metal avg `0.1048` n `20`; unknown avg `9.4803` n `1190`
- 24h: commodity avg `0.2648` n `13`; crypto_alt avg `0.7094` n `237`; crypto_major avg `-0.0963` n `8`; equity avg `-1.1036` n `151`; fx avg `-0.0131` n `6`; index avg `-0.2223` n `26`; metal avg `-0.222` n `20`; unknown avg `5.1866` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
