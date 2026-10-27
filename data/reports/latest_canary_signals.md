# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T08:22:27.528911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `13`; crypto_alt avg `-0.022` n `238`; crypto_major avg `0.0111` n `8`; equity avg `0.2025` n `154`; fx avg `0.006` n `6`; index avg `0.0339` n `27`; metal avg `0.0161` n `20`; unknown avg `0.0684` n `1230`
- 1h: commodity avg `0.099` n `13`; crypto_alt avg `0.1319` n `238`; crypto_major avg `0.2058` n `8`; equity avg `0.3762` n `154`; fx avg `0.0206` n `6`; index avg `0.0396` n `27`; metal avg `-0.0203` n `20`; unknown avg `-0.0008` n `1202`
- 4h: commodity avg `0.3606` n `13`; crypto_alt avg `0.4112` n `237`; crypto_major avg `0.0428` n `8`; equity avg `-0.3518` n `154`; fx avg `0.005` n `6`; index avg `0.019` n `27`; metal avg `-0.3181` n `20`; unknown avg `0.0066` n `1168`
- 24h: commodity avg `0.192` n `13`; crypto_alt avg `0.6558` n `237`; crypto_major avg `0.5445` n `8`; equity avg `1.1981` n `153`; fx avg `-0.0205` n `6`; index avg `0.3544` n `27`; metal avg `-0.3726` n `20`; unknown avg `1018.0309` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
