# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T14:37:43.549641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0422` n `12`; crypto_alt avg `0.3748` n `234`; crypto_major avg `0.5025` n `8`; equity avg `0.2145` n `140`; fx avg `0.0093` n `6`; index avg `0.0432` n `26`; metal avg `-0.0783` n `20`; unknown avg `-0.1061` n `908`
- 1h: commodity avg `-0.1776` n `12`; crypto_alt avg `0.3255` n `234`; crypto_major avg `0.8356` n `8`; equity avg `0.6153` n `140`; fx avg `-0.0096` n `6`; index avg `0.1276` n `26`; metal avg `-0.1912` n `20`; unknown avg `0.3758` n `884`
- 4h: commodity avg `-0.1598` n `12`; crypto_alt avg `0.5682` n `234`; crypto_major avg `1.1485` n `8`; equity avg `0.5072` n `140`; fx avg `0.0194` n `6`; index avg `0.1358` n `26`; metal avg `-0.0029` n `20`; unknown avg `10.7808` n `856`
- 24h: commodity avg `-1.0395` n `12`; crypto_alt avg `7.0876` n `234`; crypto_major avg `6.433` n `8`; equity avg `2.6047` n `140`; fx avg `-0.0604` n `6`; index avg `0.5083` n `26`; metal avg `-0.0017` n `20`; unknown avg `3.7158` n `707`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
