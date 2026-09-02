# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T07:52:34.477586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.0436` n `232`; crypto_major avg `-0.1471` n `8`; equity avg `-0.0858` n `132`; fx avg `-0.0091` n `6`; index avg `-0.025` n `26`; metal avg `-0.0488` n `20`; unknown avg `0.4093` n `792`
- 1h: commodity avg `-0.1278` n `12`; crypto_alt avg `-0.0448` n `232`; crypto_major avg `-0.0969` n `8`; equity avg `0.062` n `132`; fx avg `0.0094` n `6`; index avg `0.0041` n `26`; metal avg `0.0197` n `20`; unknown avg `0.2685` n `790`
- 4h: commodity avg `-0.0927` n `12`; crypto_alt avg `0.3222` n `232`; crypto_major avg `-0.0902` n `8`; equity avg `0.0613` n `132`; fx avg `-0.1116` n `6`; index avg `-0.013` n `26`; metal avg `0.1872` n `20`; unknown avg `0.2442` n `770`
- 24h: commodity avg `0.6278` n `12`; crypto_alt avg `-0.618` n `232`; crypto_major avg `-1.5453` n `8`; equity avg `-2.3418` n `130`; fx avg `-0.1863` n `6`; index avg `-0.4485` n `26`; metal avg `-0.8416` n `20`; unknown avg `-0.1083` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
