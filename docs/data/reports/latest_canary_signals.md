# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T03:22:24.222902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `13`; crypto_alt avg `-0.1174` n `235`; crypto_major avg `-0.0834` n `8`; equity avg `0.0069` n `150`; fx avg `0.0014` n `6`; index avg `0.0019` n `26`; metal avg `0.0059` n `20`; unknown avg `-0.1046` n `1116`
- 1h: commodity avg `0.0379` n `13`; crypto_alt avg `0.0024` n `235`; crypto_major avg `-0.078` n `8`; equity avg `0.0387` n `150`; fx avg `0.0038` n `6`; index avg `0.0046` n `26`; metal avg `0.0117` n `20`; unknown avg `0.0473` n `1114`
- 4h: commodity avg `0.0027` n `13`; crypto_alt avg `0.8716` n `235`; crypto_major avg `0.2523` n `8`; equity avg `0.0857` n `150`; fx avg `0.0056` n `6`; index avg `0.03` n `26`; metal avg `0.0237` n `20`; unknown avg `-0.0671` n `1108`
- 24h: commodity avg `-0.0295` n `13`; crypto_alt avg `2.0442` n `235`; crypto_major avg `0.1956` n `8`; equity avg `0.618` n `150`; fx avg `-0.02` n `6`; index avg `0.0871` n `26`; metal avg `0.1814` n `20`; unknown avg `18.8961` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
