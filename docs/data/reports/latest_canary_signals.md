# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T22:07:26.176343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `0.3699` n `231`; crypto_major avg `0.5323` n `8`; equity avg `-0.0256` n `127`; fx avg `0.0069` n `6`; index avg `-0.0197` n `26`; metal avg `0.0058` n `20`; unknown avg `-0.0918` n `792`
- 1h: commodity avg `0.0131` n `12`; crypto_alt avg `0.1506` n `231`; crypto_major avg `0.2199` n `8`; equity avg `-0.2296` n `127`; fx avg `0.0013` n `6`; index avg `-0.019` n `26`; metal avg `0.0013` n `20`; unknown avg `-0.1515` n `792`
- 4h: commodity avg `-0.2358` n `12`; crypto_alt avg `-0.1165` n `231`; crypto_major avg `0.0775` n `8`; equity avg `-0.0145` n `127`; fx avg `-0.0032` n `6`; index avg `0.0439` n `26`; metal avg `0.0108` n `20`; unknown avg `0.0045` n `792`
- 24h: commodity avg `0.3813` n `12`; crypto_alt avg `1.9423` n `231`; crypto_major avg `3.1011` n `8`; equity avg `-0.156` n `127`; fx avg `-0.0302` n `6`; index avg `-0.093` n `26`; metal avg `0.1382` n `20`; unknown avg `0.91` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
