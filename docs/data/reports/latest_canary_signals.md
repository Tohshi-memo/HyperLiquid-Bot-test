# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T09:07:30.535008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0511` n `13`; crypto_alt avg `-0.1323` n `237`; crypto_major avg `-0.0783` n `8`; equity avg `-0.3104` n `151`; fx avg `-0.0276` n `6`; index avg `-0.0637` n `26`; metal avg `-0.0589` n `20`; unknown avg `0.2781` n `1196`
- 1h: commodity avg `0.1329` n `13`; crypto_alt avg `-0.2408` n `237`; crypto_major avg `-0.0997` n `8`; equity avg `-0.1964` n `151`; fx avg `-0.0155` n `6`; index avg `-0.0594` n `26`; metal avg `-0.0117` n `20`; unknown avg `0.2872` n `1196`
- 4h: commodity avg `0.2609` n `13`; crypto_alt avg `-0.8733` n `237`; crypto_major avg `-0.8534` n `8`; equity avg `-0.4552` n `151`; fx avg `-0.0355` n `6`; index avg `-0.0646` n `26`; metal avg `-0.1151` n `20`; unknown avg `7.7007` n `1160`
- 24h: commodity avg `0.387` n `13`; crypto_alt avg `-0.673` n `237`; crypto_major avg `-1.2536` n `8`; equity avg `-1.7195` n `151`; fx avg `-0.0301` n `6`; index avg `-0.2885` n `26`; metal avg `-0.2588` n `20`; unknown avg `4.6947` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1828`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
