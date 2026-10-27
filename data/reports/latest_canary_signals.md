# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T13:37:30.168683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0357` n `13`; crypto_alt avg `-0.0363` n `238`; crypto_major avg `0.0063` n `8`; equity avg `0.3914` n `154`; fx avg `-0.0189` n `6`; index avg `0.0194` n `27`; metal avg `0.0741` n `20`; unknown avg `163.0486` n `1238`
- 1h: commodity avg `-0.1092` n `13`; crypto_alt avg `-0.0917` n `238`; crypto_major avg `0.0766` n `8`; equity avg `0.3097` n `154`; fx avg `-0.0144` n `6`; index avg `0.0027` n `27`; metal avg `0.0818` n `20`; unknown avg `3.4123` n `1234`
- 4h: commodity avg `-0.35` n `13`; crypto_alt avg `0.5587` n `238`; crypto_major avg `0.918` n `8`; equity avg `1.1774` n `154`; fx avg `0.0267` n `6`; index avg `0.1275` n `27`; metal avg `0.2448` n `20`; unknown avg `3.5175` n `1182`
- 24h: commodity avg `-0.2287` n `13`; crypto_alt avg `-0.1904` n `237`; crypto_major avg `0.6498` n `8`; equity avg `1.8054` n `153`; fx avg `-0.0286` n `6`; index avg `0.3536` n `27`; metal avg `-0.0025` n `20`; unknown avg `1010.2257` n `1050`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
