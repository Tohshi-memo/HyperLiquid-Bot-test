# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T16:52:33.058193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1293` n `13`; crypto_alt avg `-0.2703` n `238`; crypto_major avg `-0.2535` n `8`; equity avg `-0.4577` n `156`; fx avg `-0.0041` n `6`; index avg `-0.0613` n `27`; metal avg `-0.0224` n `20`; unknown avg `0.1419` n `1261`
- 1h: commodity avg `0.0605` n `13`; crypto_alt avg `0.0307` n `238`; crypto_major avg `-0.1741` n `8`; equity avg `-0.6615` n `156`; fx avg `0.0257` n `6`; index avg `-0.0746` n `27`; metal avg `0.0183` n `20`; unknown avg `0.0874` n `1249`
- 4h: commodity avg `0.1553` n `13`; crypto_alt avg `0.0382` n `238`; crypto_major avg `-0.3277` n `8`; equity avg `-1.64` n `156`; fx avg `-0.0148` n `6`; index avg `-0.1148` n `27`; metal avg `-0.1396` n `20`; unknown avg `6.4877` n `1149`
- 24h: commodity avg `0.5391` n `13`; crypto_alt avg `-5.5795` n `238`; crypto_major avg `-4.7969` n `8`; equity avg `-6.3068` n `156`; fx avg `-0.0962` n `6`; index avg `-0.5457` n `27`; metal avg `-0.9058` n `20`; unknown avg `55.4135` n `1038`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
