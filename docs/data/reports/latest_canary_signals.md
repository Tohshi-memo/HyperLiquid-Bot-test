# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T22:37:28.719747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `13`; crypto_alt avg `-0.1189` n `237`; crypto_major avg `-0.0867` n `8`; equity avg `-0.0516` n `154`; fx avg `-0.0013` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0152` n `20`; unknown avg `0.0826` n `1228`
- 1h: commodity avg `-0.0165` n `13`; crypto_alt avg `-0.2596` n `237`; crypto_major avg `-0.1528` n `8`; equity avg `0.0979` n `154`; fx avg `0.0144` n `6`; index avg `0.0266` n `27`; metal avg `-0.0156` n `20`; unknown avg `0.2563` n `1224`
- 4h: commodity avg `-0.0748` n `13`; crypto_alt avg `-0.4333` n `237`; crypto_major avg `-0.628` n `8`; equity avg `-0.0882` n `154`; fx avg `-0.0097` n `6`; index avg `0.0019` n `27`; metal avg `-0.0301` n `20`; unknown avg `9.6088` n `1124`
- 24h: commodity avg `-0.0375` n `13`; crypto_alt avg `-0.6172` n `237`; crypto_major avg `-0.3733` n `8`; equity avg `0.6591` n `153`; fx avg `0.0131` n `6`; index avg `-0.1206` n `27`; metal avg `-0.0893` n `20`; unknown avg `711.0525` n `980`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
