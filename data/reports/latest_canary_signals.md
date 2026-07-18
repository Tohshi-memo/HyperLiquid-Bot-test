# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T09:52:26.531615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `0.0424` n `230`; crypto_major avg `0.0437` n `8`; equity avg `-0.0091` n `96`; fx avg `0.0036` n `6`; index avg `0.0058` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.0014` n `769`
- 1h: commodity avg `0.0294` n `12`; crypto_alt avg `-0.2911` n `230`; crypto_major avg `-0.1839` n `8`; equity avg `-0.0608` n `96`; fx avg `-0.0027` n `6`; index avg `-0.0131` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0311` n `769`
- 4h: commodity avg `0.0747` n `12`; crypto_alt avg `-0.345` n `230`; crypto_major avg `-0.0858` n `8`; equity avg `-0.1688` n `96`; fx avg `0.0079` n `6`; index avg `0.0123` n `25`; metal avg `0.0136` n `20`; unknown avg `-0.0526` n `737`
- 24h: commodity avg `0.6592` n `12`; crypto_alt avg `-0.7497` n `230`; crypto_major avg `0.039` n `8`; equity avg `0.9414` n `96`; fx avg `0.0116` n `6`; index avg `0.2111` n `25`; metal avg `0.1623` n `20`; unknown avg `0.198` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
