# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T05:37:29.911965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `0.1492` n `230`; crypto_major avg `0.0927` n `8`; equity avg `0.1504` n `98`; fx avg `-0.0218` n `6`; index avg `0.0627` n `25`; metal avg `0.0995` n `20`; unknown avg `-0.3127` n `771`
- 1h: commodity avg `0.0552` n `12`; crypto_alt avg `0.2921` n `230`; crypto_major avg `0.2286` n `8`; equity avg `0.0005` n `98`; fx avg `-0.0111` n `6`; index avg `-0.0324` n `25`; metal avg `0.1072` n `20`; unknown avg `-0.3822` n `771`
- 4h: commodity avg `0.0496` n `12`; crypto_alt avg `0.6879` n `230`; crypto_major avg `0.5269` n `8`; equity avg `0.915` n `98`; fx avg `-0.0411` n `6`; index avg `0.1087` n `25`; metal avg `0.338` n `20`; unknown avg `-0.2012` n `771`
- 24h: commodity avg `-0.2877` n `12`; crypto_alt avg `3.0477` n `230`; crypto_major avg `2.6031` n `8`; equity avg `1.307` n `98`; fx avg `-0.1295` n `6`; index avg `0.2936` n `25`; metal avg `0.5775` n `20`; unknown avg `0.1797` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1464`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1202`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `667`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0858`, n `667`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0784`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0723`, n `667`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.072`, n `667`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0719`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `667`, weak_sample_signal
