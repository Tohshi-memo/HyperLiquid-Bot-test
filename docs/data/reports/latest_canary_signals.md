# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T18:22:32.771775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.1098` n `232`; crypto_major avg `0.1507` n `8`; equity avg `0.1969` n `133`; fx avg `0.0055` n `6`; index avg `0.0123` n `26`; metal avg `-0.01` n `20`; unknown avg `0.0123` n `792`
- 1h: commodity avg `0.0159` n `12`; crypto_alt avg `0.3851` n `232`; crypto_major avg `0.6151` n `8`; equity avg `0.4515` n `133`; fx avg `0.0071` n `6`; index avg `0.0332` n `26`; metal avg `0.0746` n `20`; unknown avg `16.4921` n `790`
- 4h: commodity avg `0.2532` n `12`; crypto_alt avg `-0.1833` n `232`; crypto_major avg `-0.1678` n `8`; equity avg `0.337` n `133`; fx avg `-0.0183` n `6`; index avg `0.0302` n `26`; metal avg `-0.0953` n `20`; unknown avg `15.5566` n `789`
- 24h: commodity avg `0.3829` n `12`; crypto_alt avg `0.2999` n `232`; crypto_major avg `0.0378` n `8`; equity avg `0.6918` n `133`; fx avg `-0.3615` n `6`; index avg `0.1312` n `26`; metal avg `0.3247` n `20`; unknown avg `-0.2356` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0378`, n `668`, weak_sample_signal
