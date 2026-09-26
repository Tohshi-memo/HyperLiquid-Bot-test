# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T20:07:25.873368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.1208` n `234`; crypto_major avg `-0.032` n `8`; equity avg `0.0061` n `141`; fx avg `-0.0108` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0001` n `20`; unknown avg `157.9163` n `953`
- 1h: commodity avg `0.0063` n `12`; crypto_alt avg `-0.3749` n `234`; crypto_major avg `-0.1376` n `8`; equity avg `0.0289` n `141`; fx avg `-0.0036` n `6`; index avg `-0.0003` n `26`; metal avg `0.0052` n `20`; unknown avg `156.0128` n `953`
- 4h: commodity avg `0.0333` n `12`; crypto_alt avg `-1.3235` n `234`; crypto_major avg `-0.7103` n `8`; equity avg `-0.0397` n `141`; fx avg `0.003` n `6`; index avg `-0.0128` n `26`; metal avg `0.0073` n `20`; unknown avg `9.8505` n `953`
- 24h: commodity avg `0.3053` n `12`; crypto_alt avg `1.1538` n `234`; crypto_major avg `-0.6617` n `8`; equity avg `0.0549` n `141`; fx avg `0.0133` n `6`; index avg `-0.0363` n `26`; metal avg `-0.026` n `20`; unknown avg `4.5687` n `836`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
