# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T10:52:24.759626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0342` n `13`; crypto_alt avg `0.4743` n `238`; crypto_major avg `0.7997` n `8`; equity avg `0.2122` n `155`; fx avg `0.0062` n `6`; index avg `0.0408` n `27`; metal avg `0.0348` n `20`; unknown avg `1.9221` n `1236`
- 1h: commodity avg `-0.1247` n `13`; crypto_alt avg `0.891` n `238`; crypto_major avg `1.2072` n `8`; equity avg `0.2831` n `155`; fx avg `0.0464` n `6`; index avg `-0.0168` n `27`; metal avg `0.0997` n `20`; unknown avg `2.308` n `1146`
- 4h: commodity avg `-0.0921` n `13`; crypto_alt avg `1.1345` n `238`; crypto_major avg `1.3352` n `8`; equity avg `0.2924` n `155`; fx avg `0.0752` n `6`; index avg `0.0448` n `27`; metal avg `-0.0778` n `20`; unknown avg `1.96` n `1120`
- 24h: commodity avg `-0.2944` n `13`; crypto_alt avg `-1.7877` n `238`; crypto_major avg `-0.9318` n `8`; equity avg `-1.4587` n `155`; fx avg `0.0969` n `6`; index avg `-0.0088` n `27`; metal avg `-0.3405` n `20`; unknown avg `11.0277` n `982`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
