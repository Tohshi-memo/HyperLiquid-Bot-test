# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T04:07:31.464643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `0.0399` n `230`; crypto_major avg `-0.0081` n `8`; equity avg `0.0661` n `112`; fx avg `-0.0051` n `6`; index avg `0.0129` n `25`; metal avg `0.0159` n `20`; unknown avg `-0.0969` n `783`
- 1h: commodity avg `0.0091` n `12`; crypto_alt avg `0.2635` n `230`; crypto_major avg `0.2993` n `8`; equity avg `0.0184` n `112`; fx avg `-0.0015` n `6`; index avg `0.006` n `25`; metal avg `0.0263` n `20`; unknown avg `-0.0954` n `783`
- 4h: commodity avg `0.0361` n `12`; crypto_alt avg `0.4567` n `230`; crypto_major avg `0.5017` n `8`; equity avg `-0.037` n `112`; fx avg `0.0021` n `6`; index avg `0.0031` n `25`; metal avg `-0.0136` n `20`; unknown avg `-0.1919` n `783`
- 24h: commodity avg `-0.1911` n `12`; crypto_alt avg `0.1715` n `230`; crypto_major avg `0.6859` n `8`; equity avg `1.7672` n `112`; fx avg `-0.0769` n `6`; index avg `0.2422` n `25`; metal avg `0.3111` n `20`; unknown avg `0.0129` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
