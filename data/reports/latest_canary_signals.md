# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T16:37:32.690785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1215` n `13`; crypto_alt avg `0.1664` n `238`; crypto_major avg `0.2082` n `8`; equity avg `0.036` n `156`; fx avg `-0.009` n `6`; index avg `0.0062` n `27`; metal avg `0.0342` n `20`; unknown avg `0.8245` n `1261`
- 1h: commodity avg `0.0148` n `13`; crypto_alt avg `0.239` n `238`; crypto_major avg `0.1325` n `8`; equity avg `-0.2455` n `156`; fx avg `0.0253` n `6`; index avg `-0.0131` n `27`; metal avg `0.0118` n `20`; unknown avg `-0.0448` n `1249`
- 4h: commodity avg `0.0622` n `13`; crypto_alt avg `0.2389` n `238`; crypto_major avg `-0.2016` n `8`; equity avg `-1.2534` n `156`; fx avg `-0.035` n `6`; index avg `-0.0548` n `27`; metal avg `-0.1764` n `20`; unknown avg `4.6512` n `1149`
- 24h: commodity avg `0.4532` n `13`; crypto_alt avg `-5.4301` n `238`; crypto_major avg `-4.6258` n `8`; equity avg `-5.9551` n `156`; fx avg `-0.0892` n `6`; index avg `-0.485` n `27`; metal avg `-0.8838` n `20`; unknown avg `51.9563` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
