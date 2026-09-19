# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T15:52:30.084219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.0364` n `234`; crypto_major avg `0.0221` n `8`; equity avg `0.0035` n `140`; fx avg `-0.0027` n `6`; index avg `0.0043` n `26`; metal avg `0.0022` n `20`; unknown avg `3.3731` n `943`
- 1h: commodity avg `-0.0768` n `12`; crypto_alt avg `-0.1251` n `234`; crypto_major avg `0.0459` n `8`; equity avg `-0.0003` n `140`; fx avg `-0.0151` n `6`; index avg `0.0092` n `26`; metal avg `-0.0067` n `20`; unknown avg `3.1849` n `940`
- 4h: commodity avg `-0.1418` n `12`; crypto_alt avg `-0.1696` n `234`; crypto_major avg `0.2745` n `8`; equity avg `0.0497` n `140`; fx avg `-0.0183` n `6`; index avg `0.0221` n `26`; metal avg `0.0157` n `20`; unknown avg `1.2311` n `932`
- 24h: commodity avg `-0.3077` n `12`; crypto_alt avg `2.5976` n `234`; crypto_major avg `1.7611` n `8`; equity avg `0.6724` n `140`; fx avg `0.0077` n `6`; index avg `0.1579` n `26`; metal avg `0.0628` n `20`; unknown avg `1.6863` n `806`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
