# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T12:52:25.534391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `13`; crypto_alt avg `0.038` n `239`; crypto_major avg `0.1195` n `8`; equity avg `-0.1805` n `160`; fx avg `-0.0177` n `6`; index avg `-0.0134` n `27`; metal avg `0.0102` n `20`; unknown avg `-0.1326` n `1262`
- 1h: commodity avg `-0.1527` n `13`; crypto_alt avg `0.0876` n `239`; crypto_major avg `-0.1103` n `8`; equity avg `-0.4824` n `160`; fx avg `-0.0051` n `6`; index avg `-0.0225` n `27`; metal avg `0.0155` n `20`; unknown avg `1.087` n `1250`
- 4h: commodity avg `0.073` n `13`; crypto_alt avg `-0.2744` n `239`; crypto_major avg `-0.6685` n `8`; equity avg `-1.1395` n `160`; fx avg `-0.0348` n `6`; index avg `-0.0974` n `27`; metal avg `-0.2611` n `20`; unknown avg `336.4163` n `1238`
- 24h: commodity avg `-0.4366` n `13`; crypto_alt avg `-0.5339` n `239`; crypto_major avg `-1.0258` n `8`; equity avg `2.5126` n `160`; fx avg `-0.039` n `6`; index avg `0.3201` n `27`; metal avg `-0.1197` n `20`; unknown avg `2.8441` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2335`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
