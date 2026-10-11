# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T11:22:27.888330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `0.1627` n `235`; crypto_major avg `0.0527` n `8`; equity avg `0.0035` n `150`; fx avg `0.001` n `6`; index avg `0.0001` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.0931` n `1117`
- 1h: commodity avg `0.0032` n `13`; crypto_alt avg `-0.1526` n `235`; crypto_major avg `0.0079` n `8`; equity avg `-0.012` n `150`; fx avg `0.007` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.1118` n `1115`
- 4h: commodity avg `0.035` n `13`; crypto_alt avg `-0.2171` n `235`; crypto_major avg `0.0606` n `8`; equity avg `0.0408` n `150`; fx avg `0.0141` n `6`; index avg `0.0005` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.6447` n `1099`
- 24h: commodity avg `0.4399` n `13`; crypto_alt avg `1.0122` n `235`; crypto_major avg `0.0639` n `8`; equity avg `0.0897` n `150`; fx avg `0.0132` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.8726` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
