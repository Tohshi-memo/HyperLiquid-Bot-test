# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T14:37:36.762436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `12`; crypto_alt avg `0.2449` n `230`; crypto_major avg `0.2427` n `8`; equity avg `0.0692` n `114`; fx avg `-0.0065` n `6`; index avg `0.0063` n `25`; metal avg `-0.046` n `20`; unknown avg `-0.0756` n `795`
- 1h: commodity avg `-0.1541` n `12`; crypto_alt avg `0.3771` n `230`; crypto_major avg `0.5776` n `8`; equity avg `-0.6907` n `114`; fx avg `0.0049` n `6`; index avg `-0.0779` n `25`; metal avg `-0.1518` n `20`; unknown avg `-0.0531` n `795`
- 4h: commodity avg `0.0682` n `12`; crypto_alt avg `0.4451` n `230`; crypto_major avg `0.4666` n `8`; equity avg `-0.6575` n `114`; fx avg `0.0233` n `6`; index avg `-0.0542` n `25`; metal avg `-0.1932` n `20`; unknown avg `-0.1182` n `795`
- 24h: commodity avg `0.4922` n `12`; crypto_alt avg `-0.3177` n `230`; crypto_major avg `0.5536` n `8`; equity avg `-3.3389` n `114`; fx avg `-0.0255` n `6`; index avg `-0.6277` n `25`; metal avg `-0.5243` n `20`; unknown avg `-0.1029` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
