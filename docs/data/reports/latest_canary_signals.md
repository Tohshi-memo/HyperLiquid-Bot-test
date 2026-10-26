# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T18:07:43.399377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0837` n `13`; crypto_alt avg `0.1738` n `237`; crypto_major avg `0.1495` n `8`; equity avg `0.21` n `154`; fx avg `-0.0039` n `6`; index avg `0.0416` n `27`; metal avg `0.0203` n `20`; unknown avg `0.0686` n `1236`
- 1h: commodity avg `-0.1924` n `13`; crypto_alt avg `-0.0507` n `237`; crypto_major avg `0.0781` n `8`; equity avg `0.2373` n `154`; fx avg `0.0104` n `6`; index avg `0.0226` n `27`; metal avg `-0.0597` n `20`; unknown avg `-0.1153` n `1238`
- 4h: commodity avg `0.1342` n `13`; crypto_alt avg `0.8358` n `237`; crypto_major avg `1.0407` n `8`; equity avg `2.1325` n `154`; fx avg `0.0244` n `6`; index avg `0.2494` n `27`; metal avg `0.1942` n `20`; unknown avg `635.4389` n `1166`
- 24h: commodity avg `-0.2593` n `13`; crypto_alt avg `-0.2733` n `237`; crypto_major avg `0.1824` n `8`; equity avg `0.9984` n `153`; fx avg `0.0618` n `6`; index avg `-0.0374` n `27`; metal avg `0.0773` n `20`; unknown avg `781.5041` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1865`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
