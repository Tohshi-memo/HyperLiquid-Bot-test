# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T11:52:27.694039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0832` n `13`; crypto_alt avg `-0.051` n `238`; crypto_major avg `0.0228` n `8`; equity avg `-0.0041` n `154`; fx avg `0.0086` n `6`; index avg `0.0039` n `27`; metal avg `-0.0178` n `20`; unknown avg `-0.2528` n `1238`
- 1h: commodity avg `0.0339` n `13`; crypto_alt avg `-0.1342` n `238`; crypto_major avg `-0.0837` n `8`; equity avg `0.1999` n `154`; fx avg `0.007` n `6`; index avg `0.017` n `27`; metal avg `0.0034` n `20`; unknown avg `7.7934` n `1188`
- 4h: commodity avg `-0.2913` n `13`; crypto_alt avg `-0.5178` n `238`; crypto_major avg `-0.1272` n `8`; equity avg `1.0975` n `154`; fx avg `-0.0176` n `6`; index avg `0.1455` n `27`; metal avg `0.1101` n `20`; unknown avg `14.5799` n `1156`
- 24h: commodity avg `-0.1233` n `13`; crypto_alt avg `-0.5515` n `237`; crypto_major avg `-0.2064` n `8`; equity avg `1.0115` n `153`; fx avg `-0.0442` n `6`; index avg `0.3363` n `27`; metal avg `-0.2885` n `20`; unknown avg `1049.5904` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
