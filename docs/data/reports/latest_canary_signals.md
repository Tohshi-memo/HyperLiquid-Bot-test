# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T16:08:14.480166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.65` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0223` n `13`; crypto_alt avg `-0.062` n `238`; crypto_major avg `0.0408` n `8`; equity avg `0.0653` n `155`; fx avg `0.0231` n `6`; index avg `0.012` n `27`; metal avg `0.0017` n `20`; unknown avg `0.4841` n `1226`
- 1h: commodity avg `0.1659` n `13`; crypto_alt avg `-0.0159` n `238`; crypto_major avg `-0.0611` n `8`; equity avg `0.1632` n `155`; fx avg `0.0264` n `6`; index avg `0.0216` n `27`; metal avg `-0.0283` n `20`; unknown avg `1.4648` n `1226`
- 4h: commodity avg `0.3969` n `13`; crypto_alt avg `-0.7489` n `238`; crypto_major avg `-0.922` n `8`; equity avg `-0.2321` n `155`; fx avg `0.0816` n `6`; index avg `0.0602` n `27`; metal avg `-0.0784` n `20`; unknown avg `2.0662` n `1150`
- 24h: commodity avg `0.6868` n `13`; crypto_alt avg `0.0638` n `238`; crypto_major avg `0.052` n `8`; equity avg `1.0939` n `154`; fx avg `0.2478` n `6`; index avg `0.2287` n `27`; metal avg `-0.1731` n `20`; unknown avg `3.2056` n `1098`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
