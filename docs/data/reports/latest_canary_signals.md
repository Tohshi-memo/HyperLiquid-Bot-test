# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T19:22:34.837039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0332` n `13`; crypto_alt avg `0.3799` n `237`; crypto_major avg `0.2898` n `8`; equity avg `0.1664` n `154`; fx avg `-0.0033` n `6`; index avg `0.0361` n `27`; metal avg `0.0372` n `20`; unknown avg `0.0384` n `1238`
- 1h: commodity avg `0.0838` n `13`; crypto_alt avg `-0.0897` n `237`; crypto_major avg `-0.1527` n `8`; equity avg `-0.0608` n `154`; fx avg `-0.0132` n `6`; index avg `-0.0118` n `27`; metal avg `-0.0608` n `20`; unknown avg `-0.373` n `1236`
- 4h: commodity avg `0.0157` n `13`; crypto_alt avg `-0.8231` n `237`; crypto_major avg `-0.4298` n `8`; equity avg `-0.1883` n `154`; fx avg `-0.0246` n `6`; index avg `-0.0552` n `27`; metal avg `-0.1475` n `20`; unknown avg `-0.3622` n `1230`
- 24h: commodity avg `-0.1182` n `13`; crypto_alt avg `-0.3822` n `237`; crypto_major avg `-0.0058` n `8`; equity avg `0.7039` n `153`; fx avg `0.0279` n `6`; index avg `-0.0857` n `27`; metal avg `0.0182` n `20`; unknown avg `779.0848` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
