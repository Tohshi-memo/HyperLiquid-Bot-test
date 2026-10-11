# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T06:52:27.755349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `13`; crypto_alt avg `0.2813` n `235`; crypto_major avg `0.1529` n `8`; equity avg `0.0343` n `150`; fx avg `0.0` n `6`; index avg `0.0013` n `26`; metal avg `0.0126` n `20`; unknown avg `0.848` n `1117`
- 1h: commodity avg `0.0466` n `13`; crypto_alt avg `0.4841` n `235`; crypto_major avg `0.1647` n `8`; equity avg `0.0327` n `150`; fx avg `0.0072` n `6`; index avg `0.0028` n `26`; metal avg `0.0179` n `20`; unknown avg `0.6142` n `1099`
- 4h: commodity avg `0.1` n `13`; crypto_alt avg `-0.0581` n `235`; crypto_major avg `-0.2079` n `8`; equity avg `-0.0748` n `150`; fx avg `0.0056` n `6`; index avg `-0.015` n `26`; metal avg `0.0054` n `20`; unknown avg `0.6916` n `1093`
- 24h: commodity avg `0.1445` n `13`; crypto_alt avg `1.0052` n `235`; crypto_major avg `0.0705` n `8`; equity avg `0.0354` n `150`; fx avg `-0.005` n `6`; index avg `-0.0169` n `26`; metal avg `0.0169` n `20`; unknown avg `0.4933` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
