# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T06:37:27.876483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0406` n `13`; crypto_alt avg `0.0753` n `237`; crypto_major avg `0.0691` n `8`; equity avg `-0.0162` n `154`; fx avg `0.0053` n `6`; index avg `0.0276` n `27`; metal avg `-0.029` n `20`; unknown avg `0.7999` n `1238`
- 1h: commodity avg `0.1064` n `13`; crypto_alt avg `0.1795` n `237`; crypto_major avg `-0.008` n `8`; equity avg `-0.1079` n `154`; fx avg `0.0132` n `6`; index avg `-0.0038` n `27`; metal avg `-0.1287` n `20`; unknown avg `0.0867` n `1220`
- 4h: commodity avg `0.1142` n `13`; crypto_alt avg `-0.0739` n `237`; crypto_major avg `-0.2786` n `8`; equity avg `-1.1783` n `154`; fx avg `-0.0057` n `6`; index avg `-0.0323` n `27`; metal avg `-0.2852` n `20`; unknown avg `1.2842` n `1198`
- 24h: commodity avg `0.1253` n `13`; crypto_alt avg `0.201` n `237`; crypto_major avg `0.1786` n `8`; equity avg `0.6222` n `153`; fx avg `-0.0241` n `6`; index avg `0.1133` n `27`; metal avg `-0.2693` n `20`; unknown avg `1110.8728` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
