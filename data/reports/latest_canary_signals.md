# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T02:07:39.993040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.87` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.0064` n `228`; crypto_major avg `-0.0403` n `8`; equity avg `-0.2275` n `88`; fx avg `0.002` n `6`; index avg `-0.0852` n `23`; metal avg `-0.0621` n `20`; unknown avg `0.3433` n `765`
- 1h: commodity avg `-0.0826` n `12`; crypto_alt avg `0.178` n `228`; crypto_major avg `0.5765` n `8`; equity avg `-0.5463` n `88`; fx avg `-0.001` n `6`; index avg `-0.1736` n `23`; metal avg `-0.3295` n `20`; unknown avg `1.9401` n `765`
- 4h: commodity avg `-0.0944` n `12`; crypto_alt avg `-0.3558` n `228`; crypto_major avg `-0.0984` n `8`; equity avg `-0.9543` n `88`; fx avg `0.077` n `6`; index avg `-0.3081` n `23`; metal avg `-0.5874` n `20`; unknown avg `-0.6454` n `765`
- 24h: commodity avg `0.0108` n `12`; crypto_alt avg `-1.5338` n `228`; crypto_major avg `-1.1619` n `8`; equity avg `0.4269` n `88`; fx avg `0.1491` n `6`; index avg `-0.0157` n `23`; metal avg `-0.1415` n `20`; unknown avg `6.8143` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
