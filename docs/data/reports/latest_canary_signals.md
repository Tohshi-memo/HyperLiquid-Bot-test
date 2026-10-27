# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T08:52:23.857610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `0.0483` n `238`; crypto_major avg `-0.0844` n `8`; equity avg `0.0515` n `154`; fx avg `0.0089` n `6`; index avg `0.0543` n `27`; metal avg `-0.0064` n `20`; unknown avg `2.2586` n `1238`
- 1h: commodity avg `0.0095` n `13`; crypto_alt avg `-0.3511` n `238`; crypto_major avg `-0.3171` n `8`; equity avg `0.2095` n `154`; fx avg `-0.0048` n `6`; index avg `0.0457` n `27`; metal avg `-0.0346` n `20`; unknown avg `199.5697` n `1204`
- 4h: commodity avg `0.3438` n `13`; crypto_alt avg `0.1896` n `237`; crypto_major avg `-0.023` n `8`; equity avg `-0.3379` n `154`; fx avg `0.0083` n `6`; index avg `-0.0577` n `27`; metal avg `-0.256` n `20`; unknown avg `1.1279` n `1172`
- 24h: commodity avg `0.2802` n `13`; crypto_alt avg `-0.5073` n `237`; crypto_major avg `-0.2258` n `8`; equity avg `0.5862` n `153`; fx avg `-0.0206` n `6`; index avg `0.3` n `27`; metal avg `-0.4178` n `20`; unknown avg `1015.8252` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1976`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
