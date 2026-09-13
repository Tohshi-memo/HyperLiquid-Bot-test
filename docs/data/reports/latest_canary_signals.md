# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T04:07:27.798490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.119` n `233`; crypto_major avg `0.0304` n `8`; equity avg `-0.0324` n `136`; fx avg `0.0031` n `6`; index avg `-0.0046` n `26`; metal avg `0.0034` n `20`; unknown avg `-0.0595` n `836`
- 1h: commodity avg `0.0264` n `12`; crypto_alt avg `-0.0049` n `233`; crypto_major avg `-0.187` n `8`; equity avg `-0.0738` n `136`; fx avg `0.0029` n `6`; index avg `-0.0025` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.0914` n `836`
- 4h: commodity avg `0.0206` n `12`; crypto_alt avg `0.3618` n `233`; crypto_major avg `-0.1702` n `8`; equity avg `-0.1808` n `136`; fx avg `0.0075` n `6`; index avg `-0.0359` n `26`; metal avg `0.0042` n `20`; unknown avg `3.6916` n `806`
- 24h: commodity avg `0.0288` n `12`; crypto_alt avg `1.0348` n `233`; crypto_major avg `-0.0073` n `8`; equity avg `-0.5068` n `136`; fx avg `-0.0098` n `6`; index avg `-0.0615` n `26`; metal avg `0.0491` n `20`; unknown avg `-0.3372` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
