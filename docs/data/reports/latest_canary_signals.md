# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T04:07:23.894818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.0508` n `232`; crypto_major avg `-0.1483` n `8`; equity avg `-0.0628` n `132`; fx avg `-0.0056` n `6`; index avg `-0.0188` n `26`; metal avg `0.0291` n `20`; unknown avg `2.3702` n `790`
- 1h: commodity avg `-0.0402` n `12`; crypto_alt avg `-0.1419` n `232`; crypto_major avg `-0.0622` n `8`; equity avg `-0.0732` n `132`; fx avg `-0.0113` n `6`; index avg `-0.0408` n `26`; metal avg `-0.004` n `20`; unknown avg `2.561` n `790`
- 4h: commodity avg `-0.0821` n `12`; crypto_alt avg `0.2218` n `232`; crypto_major avg `-0.1074` n `8`; equity avg `-0.2687` n `132`; fx avg `-0.0465` n `6`; index avg `-0.087` n `26`; metal avg `-0.1763` n `20`; unknown avg `2.9913` n `790`
- 24h: commodity avg `0.8501` n `12`; crypto_alt avg `-0.775` n `232`; crypto_major avg `-1.912` n `8`; equity avg `-2.5227` n `130`; fx avg `-0.0796` n `6`; index avg `-0.4632` n `26`; metal avg `-1.0881` n `20`; unknown avg `0.0156` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0365`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0348`, n `668`, weak_sample_signal
