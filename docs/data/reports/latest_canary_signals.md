# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T03:07:27.443661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `13`; crypto_alt avg `-0.3405` n `237`; crypto_major avg `-0.2335` n `8`; equity avg `-0.0847` n `154`; fx avg `0.0021` n `6`; index avg `-0.0177` n `27`; metal avg `-0.0189` n `20`; unknown avg `-0.1418` n `1232`
- 1h: commodity avg `-0.0381` n `13`; crypto_alt avg `-0.5334` n `237`; crypto_major avg `-0.4125` n `8`; equity avg `-0.2968` n `154`; fx avg `0.0313` n `6`; index avg `-0.034` n `27`; metal avg `-0.0346` n `20`; unknown avg `1.3561` n `1232`
- 4h: commodity avg `-0.0931` n `13`; crypto_alt avg `-0.2509` n `237`; crypto_major avg `0.1184` n `8`; equity avg `0.1876` n `154`; fx avg `0.0224` n `6`; index avg `0.1041` n `27`; metal avg `-0.0798` n `20`; unknown avg `0.503` n `1224`
- 24h: commodity avg `0.0292` n `13`; crypto_alt avg `-0.286` n `237`; crypto_major avg `0.3624` n `8`; equity avg `1.6296` n `153`; fx avg `0.0202` n `6`; index avg `0.0622` n `27`; metal avg `-0.1625` n `20`; unknown avg `1000.1466` n `1000`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
