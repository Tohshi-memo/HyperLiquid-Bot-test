# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T15:52:25.751374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0693` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0723` n `12`; crypto_alt avg `0.2609` n `234`; crypto_major avg `0.0401` n `8`; equity avg `0.0061` n `141`; fx avg `0.0011` n `6`; index avg `0.012` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.0533` n `962`
- 1h: commodity avg `-0.157` n `12`; crypto_alt avg `-0.191` n `234`; crypto_major avg `-0.1363` n `8`; equity avg `0.0089` n `141`; fx avg `0.0059` n `6`; index avg `0.0236` n `26`; metal avg `0.0025` n `20`; unknown avg `5.7739` n `960`
- 4h: commodity avg `-0.1986` n `12`; crypto_alt avg `-1.2171` n `234`; crypto_major avg `-1.0697` n `8`; equity avg `-0.0788` n `141`; fx avg `0.011` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0129` n `20`; unknown avg `9.3508` n `954`
- 24h: commodity avg `-0.1254` n `12`; crypto_alt avg `-1.514` n `234`; crypto_major avg `-0.6714` n `8`; equity avg `0.1845` n `141`; fx avg `-0.0168` n `6`; index avg `0.0161` n `26`; metal avg `-0.0116` n `20`; unknown avg `112.504` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
