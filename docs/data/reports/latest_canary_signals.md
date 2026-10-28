# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T12:52:30.653792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0386` n `13`; crypto_alt avg `-0.0388` n `238`; crypto_major avg `0.0406` n `8`; equity avg `-0.0367` n `154`; fx avg `-0.0162` n `6`; index avg `-0.0041` n `27`; metal avg `0.0072` n `20`; unknown avg `-0.0493` n `1239`
- 1h: commodity avg `0.0859` n `13`; crypto_alt avg `-1.1369` n `238`; crypto_major avg `-0.9149` n `8`; equity avg `-0.373` n `154`; fx avg `0.0102` n `6`; index avg `-0.0196` n `27`; metal avg `0.0956` n `20`; unknown avg `0.7901` n `1227`
- 4h: commodity avg `0.2325` n `13`; crypto_alt avg `-0.919` n `238`; crypto_major avg `-0.8527` n `8`; equity avg `-0.1499` n `154`; fx avg `0.0441` n `6`; index avg `0.0188` n `27`; metal avg `0.0562` n `20`; unknown avg `1.2293` n `1196`
- 24h: commodity avg `0.2443` n `13`; crypto_alt avg `0.4773` n `238`; crypto_major avg `0.7569` n `8`; equity avg `2.3856` n `154`; fx avg `0.0972` n `6`; index avg `0.3424` n `27`; metal avg `0.2937` n `20`; unknown avg `6.967` n `1068`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
