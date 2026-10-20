# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T03:52:36.757787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `0.2012` n `237`; crypto_major avg `0.1198` n `8`; equity avg `-0.091` n `151`; fx avg `-0.0005` n `6`; index avg `-0.0229` n `26`; metal avg `0.0016` n `20`; unknown avg `0.2741` n `1198`
- 1h: commodity avg `0.0462` n `13`; crypto_alt avg `0.3743` n `237`; crypto_major avg `0.2398` n `8`; equity avg `-0.2213` n `151`; fx avg `-0.0094` n `6`; index avg `-0.0485` n `26`; metal avg `0.0674` n `20`; unknown avg `8.1676` n `1196`
- 4h: commodity avg `0.0991` n `13`; crypto_alt avg `0.468` n `237`; crypto_major avg `0.1213` n `8`; equity avg `-0.3411` n `151`; fx avg `0.0054` n `6`; index avg `-0.1146` n `26`; metal avg `0.1364` n `20`; unknown avg `7.8465` n `1190`
- 24h: commodity avg `0.3205` n `13`; crypto_alt avg `0.7331` n `237`; crypto_major avg `-0.1028` n `8`; equity avg `-0.8984` n `151`; fx avg `-0.0311` n `6`; index avg `-0.1581` n `26`; metal avg `-0.2053` n `20`; unknown avg `5.1675` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
