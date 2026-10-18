# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T04:52:26.955872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `13`; crypto_alt avg `0.0066` n `237`; crypto_major avg `-0.0194` n `8`; equity avg `0.0467` n `151`; fx avg `0.0006` n `6`; index avg `0.0066` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.0609` n `1193`
- 1h: commodity avg `-0.0187` n `13`; crypto_alt avg `-0.5492` n `237`; crypto_major avg `-0.3635` n `8`; equity avg `-0.0727` n `151`; fx avg `0.0008` n `6`; index avg `0.0136` n `26`; metal avg `-0.0057` n `20`; unknown avg `-0.0591` n `1185`
- 4h: commodity avg `0.0639` n `13`; crypto_alt avg `-0.1449` n `237`; crypto_major avg `0.3151` n `8`; equity avg `0.0978` n `151`; fx avg `-0.0185` n `6`; index avg `0.0219` n `26`; metal avg `0.0122` n `20`; unknown avg `-0.0592` n `1185`
- 24h: commodity avg `-0.1309` n `13`; crypto_alt avg `-2.5458` n `236`; crypto_major avg `-0.5035` n `8`; equity avg `-0.8083` n `151`; fx avg `-0.0461` n `6`; index avg `-0.0853` n `26`; metal avg `-0.062` n `20`; unknown avg `3.6732` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.168`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1353`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1079`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0815`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
