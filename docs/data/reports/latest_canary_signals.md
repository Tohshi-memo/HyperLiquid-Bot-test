# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T22:22:31.040666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `0.0572` n `234`; crypto_major avg `0.0156` n `8`; equity avg `-0.0089` n `140`; fx avg `0.0006` n `6`; index avg `-0.0085` n `26`; metal avg `0.0119` n `20`; unknown avg `-0.0501` n `942`
- 1h: commodity avg `-0.0111` n `12`; crypto_alt avg `0.0526` n `234`; crypto_major avg `0.1788` n `8`; equity avg `0.027` n `140`; fx avg `-0.0153` n `6`; index avg `-0.0027` n `26`; metal avg `0.0164` n `20`; unknown avg `25.3854` n `914`
- 4h: commodity avg `-0.0881` n `12`; crypto_alt avg `1.0428` n `234`; crypto_major avg `0.6081` n `8`; equity avg `0.6179` n `140`; fx avg `0.0369` n `6`; index avg `0.1119` n `26`; metal avg `-0.1097` n `20`; unknown avg `2.8099` n `872`
- 24h: commodity avg `-0.1151` n `12`; crypto_alt avg `7.5624` n `234`; crypto_major avg `7.4654` n `8`; equity avg `1.4151` n `140`; fx avg `0.2376` n `6`; index avg `0.0619` n `26`; metal avg `0.3796` n `20`; unknown avg `4.4424` n `735`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
