# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T17:46:07.194476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.0703` n `230`; crypto_major avg `-0.071` n `8`; equity avg `0.052` n `113`; fx avg `-0.0025` n `6`; index avg `0.0055` n `25`; metal avg `-0.0098` n `20`; unknown avg `1.3985` n `786`
- 1h: commodity avg `0.0357` n `12`; crypto_alt avg `0.1744` n `230`; crypto_major avg `0.1146` n `8`; equity avg `0.2808` n `113`; fx avg `0.0147` n `6`; index avg `0.0209` n `25`; metal avg `0.024` n `20`; unknown avg `0.4796` n `786`
- 4h: commodity avg `0.0848` n `12`; crypto_alt avg `-0.4451` n `230`; crypto_major avg `-0.1421` n `8`; equity avg `0.6637` n `113`; fx avg `0.008` n `6`; index avg `-0.0047` n `25`; metal avg `-0.2363` n `20`; unknown avg `0.2511` n `786`
- 24h: commodity avg `0.0223` n `12`; crypto_alt avg `-0.0501` n `230`; crypto_major avg `0.8252` n `8`; equity avg `3.8756` n `113`; fx avg `0.047` n `6`; index avg `0.4146` n `25`; metal avg `0.1751` n `20`; unknown avg `0.139` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2269`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
