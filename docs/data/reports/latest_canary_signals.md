# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T09:07:25.780204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.115` n `13`; crypto_alt avg `0.0719` n `238`; crypto_major avg `0.1357` n `8`; equity avg `0.2414` n `154`; fx avg `-0.0176` n `6`; index avg `0.0118` n `27`; metal avg `0.0874` n `20`; unknown avg `0.0518` n `1236`
- 1h: commodity avg `-0.1068` n `13`; crypto_alt avg `-0.1334` n `238`; crypto_major avg `-0.0673` n `8`; equity avg `0.3366` n `154`; fx avg `-0.0222` n `6`; index avg `0.0678` n `27`; metal avg `0.0757` n `20`; unknown avg `195.4426` n `1226`
- 4h: commodity avg `0.2569` n `13`; crypto_alt avg `0.0707` n `237`; crypto_major avg `-0.0343` n `8`; equity avg `-0.2129` n `154`; fx avg `-0.0071` n `6`; index avg `-0.0701` n `27`; metal avg `-0.1338` n `20`; unknown avg `0.5187` n `1172`
- 24h: commodity avg `0.208` n `13`; crypto_alt avg `-0.093` n `237`; crypto_major avg `0.1448` n `8`; equity avg `0.8157` n `153`; fx avg `-0.0437` n `6`; index avg `0.2951` n `27`; metal avg `-0.3106` n `20`; unknown avg `1045.6834` n `1040`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2028`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
