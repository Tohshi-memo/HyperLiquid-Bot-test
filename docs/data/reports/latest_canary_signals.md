# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T23:52:23.022197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.2392` n `232`; crypto_major avg `0.2395` n `8`; equity avg `0.0146` n `133`; fx avg `0.0129` n `6`; index avg `0.0193` n `26`; metal avg `0.0335` n `20`; unknown avg `0.1136` n `792`
- 1h: commodity avg `-0.0187` n `12`; crypto_alt avg `0.3921` n `232`; crypto_major avg `0.4583` n `8`; equity avg `0.1298` n `133`; fx avg `0.0073` n `6`; index avg `0.0204` n `26`; metal avg `0.0274` n `20`; unknown avg `0.2557` n `790`
- 4h: commodity avg `0.0016` n `12`; crypto_alt avg `0.4249` n `232`; crypto_major avg `0.4282` n `8`; equity avg `0.1565` n `133`; fx avg `-0.0061` n `6`; index avg `0.0195` n `26`; metal avg `-0.0218` n `20`; unknown avg `16.6156` n `772`
- 24h: commodity avg `0.1465` n `12`; crypto_alt avg `-0.126` n `232`; crypto_major avg `-0.2091` n `8`; equity avg `1.1785` n `133`; fx avg `-0.3559` n `6`; index avg `0.1423` n `26`; metal avg `0.4519` n `20`; unknown avg `-0.1477` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0466`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0439`, n `668`, weak_sample_signal
