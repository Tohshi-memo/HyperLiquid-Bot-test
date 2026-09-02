# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T13:37:31.908213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0657` n `12`; crypto_alt avg `-0.1435` n `232`; crypto_major avg `-0.1375` n `8`; equity avg `-0.0255` n `133`; fx avg `-0.0767` n `6`; index avg `0.0264` n `26`; metal avg `0.1635` n `20`; unknown avg `-0.0431` n `791`
- 1h: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.3277` n `232`; crypto_major avg `-0.1876` n `8`; equity avg `0.0525` n `133`; fx avg `-0.0846` n `6`; index avg `0.0214` n `26`; metal avg `0.292` n `20`; unknown avg `-0.0048` n `789`
- 4h: commodity avg `-0.1787` n `12`; crypto_alt avg `-0.494` n `232`; crypto_major avg `-0.034` n `8`; equity avg `0.6723` n `133`; fx avg `-0.155` n `6`; index avg `0.1565` n `26`; metal avg `0.5842` n `20`; unknown avg `0.7067` n `789`
- 24h: commodity avg `0.4566` n `12`; crypto_alt avg `-1.2398` n `232`; crypto_major avg `-1.8929` n `8`; equity avg `-0.596` n `132`; fx avg `-0.3425` n `6`; index avg `-0.107` n `26`; metal avg `0.1364` n `20`; unknown avg `-0.0778` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
