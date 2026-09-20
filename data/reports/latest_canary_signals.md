# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T04:37:32.710452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4051` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `0.3158` n `234`; crypto_major avg `0.2599` n `8`; equity avg `0.0101` n `140`; fx avg `0.0027` n `6`; index avg `0.0048` n `26`; metal avg `-0.0079` n `20`; unknown avg `0.4125` n `933`
- 1h: commodity avg `-0.0192` n `12`; crypto_alt avg `0.4013` n `234`; crypto_major avg `0.197` n `8`; equity avg `0.0181` n `140`; fx avg `-0.003` n `6`; index avg `0.0008` n `26`; metal avg `-0.0146` n `20`; unknown avg `18.2555` n `925`
- 4h: commodity avg `0.2167` n `12`; crypto_alt avg `-1.5902` n `234`; crypto_major avg `-1.4608` n `8`; equity avg `-0.3961` n `140`; fx avg `0.0079` n `6`; index avg `-0.0557` n `26`; metal avg `-0.0475` n `20`; unknown avg `4.6898` n `925`
- 24h: commodity avg `0.2511` n `12`; crypto_alt avg `-0.1155` n `234`; crypto_major avg `-1.5122` n `8`; equity avg `-0.225` n `140`; fx avg `-0.0547` n `6`; index avg `-0.0532` n `26`; metal avg `-0.0284` n `20`; unknown avg `4.5802` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
