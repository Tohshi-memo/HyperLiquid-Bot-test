# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T15:22:29.479509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `12`; crypto_alt avg `0.0117` n `232`; crypto_major avg `0.1108` n `8`; equity avg `0.0447` n `133`; fx avg `-0.0238` n `6`; index avg `0.0094` n `26`; metal avg `-0.0471` n `20`; unknown avg `0.7118` n `791`
- 1h: commodity avg `0.2316` n `12`; crypto_alt avg `-0.6575` n `232`; crypto_major avg `-0.5881` n `8`; equity avg `-0.3757` n `133`; fx avg `-0.0307` n `6`; index avg `-0.0202` n `26`; metal avg `-0.1174` n `20`; unknown avg `0.1202` n `789`
- 4h: commodity avg `0.3238` n `12`; crypto_alt avg `0.2167` n `232`; crypto_major avg `0.696` n `8`; equity avg `0.7158` n `133`; fx avg `-0.1294` n `6`; index avg `0.1864` n `26`; metal avg `0.3868` n `20`; unknown avg `0.3131` n `789`
- 24h: commodity avg `0.7069` n `12`; crypto_alt avg `-1.3368` n `232`; crypto_major avg `-1.5687` n `8`; equity avg `-0.467` n `132`; fx avg `-0.3657` n `6`; index avg `-0.0585` n `26`; metal avg `0.1026` n `20`; unknown avg `-0.024` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
