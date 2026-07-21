# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T06:37:24.731702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `0.1603` n `230`; crypto_major avg `0.2785` n `8`; equity avg `0.0298` n `98`; fx avg `0.0045` n `6`; index avg `0.0208` n `25`; metal avg `0.0335` n `20`; unknown avg `0.062` n `771`
- 1h: commodity avg `-0.0155` n `12`; crypto_alt avg `0.2883` n `230`; crypto_major avg `0.4143` n `8`; equity avg `0.3383` n `98`; fx avg `0.0252` n `6`; index avg `0.05` n `25`; metal avg `0.1812` n `20`; unknown avg `-0.0129` n `755`
- 4h: commodity avg `0.01` n `12`; crypto_alt avg `1.0619` n `230`; crypto_major avg `1.0199` n `8`; equity avg `1.4268` n `98`; fx avg `-0.0286` n `6`; index avg `0.168` n `25`; metal avg `0.3989` n `20`; unknown avg `0.1012` n `755`
- 24h: commodity avg `-0.3882` n `12`; crypto_alt avg `3.5934` n `230`; crypto_major avg `3.4819` n `8`; equity avg `1.9391` n `98`; fx avg `-0.0779` n `6`; index avg `0.3794` n `25`; metal avg `0.7706` n `20`; unknown avg `0.2702` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0792`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0686`, n `666`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0669`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0659`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
