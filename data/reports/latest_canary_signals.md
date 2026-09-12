# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T19:37:26.542886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.2013` n `233`; crypto_major avg `-0.1572` n `8`; equity avg `-0.1694` n `136`; fx avg `0.0006` n `6`; index avg `-0.0173` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.11` n `838`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `-0.3495` n `233`; crypto_major avg `-0.2603` n `8`; equity avg `-0.1861` n `136`; fx avg `0.0007` n `6`; index avg `-0.0223` n `26`; metal avg `-0.0049` n `20`; unknown avg `2.5877` n `828`
- 4h: commodity avg `0.0754` n `12`; crypto_alt avg `-0.5372` n `233`; crypto_major avg `-0.591` n `8`; equity avg `-0.1923` n `136`; fx avg `-0.0071` n `6`; index avg `-0.0295` n `26`; metal avg `0.0075` n `20`; unknown avg `0.0272` n `782`
- 24h: commodity avg `-0.2023` n `12`; crypto_alt avg `0.9812` n `233`; crypto_major avg `-0.2598` n `8`; equity avg `-0.2111` n `136`; fx avg `-0.0364` n `6`; index avg `-0.013` n `26`; metal avg `0.0141` n `20`; unknown avg `0.8671` n `710`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0437`, n `668`, weak_sample_signal
