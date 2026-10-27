# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T06:52:32.236780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0492` n `13`; crypto_alt avg `-0.1301` n `237`; crypto_major avg `-0.1891` n `8`; equity avg `-0.0956` n `154`; fx avg `-0.0028` n `6`; index avg `-0.026` n `27`; metal avg `-0.0351` n `20`; unknown avg `1.7558` n `1238`
- 1h: commodity avg `0.1503` n `13`; crypto_alt avg `-0.3355` n `237`; crypto_major avg `-0.4385` n `8`; equity avg `-0.3053` n `154`; fx avg `0.0058` n `6`; index avg `-0.0342` n `27`; metal avg `-0.1699` n `20`; unknown avg `0.2306` n `1220`
- 4h: commodity avg `0.174` n `13`; crypto_alt avg `-0.192` n `237`; crypto_major avg `-0.469` n `8`; equity avg `-1.1851` n `154`; fx avg `-0.0256` n `6`; index avg `-0.0557` n `27`; metal avg `-0.2511` n `20`; unknown avg `0.3757` n `1198`
- 24h: commodity avg `0.1895` n `13`; crypto_alt avg `-0.0428` n `237`; crypto_major avg `-0.0639` n `8`; equity avg `0.62` n `153`; fx avg `-0.0326` n `6`; index avg `0.1018` n `27`; metal avg `-0.3054` n `20`; unknown avg `1110.129` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
