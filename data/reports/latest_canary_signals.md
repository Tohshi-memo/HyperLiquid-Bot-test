# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T00:07:31.389114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `13`; crypto_alt avg `-0.0296` n `235`; crypto_major avg `-0.1295` n `8`; equity avg `-0.0083` n `150`; fx avg `0.0055` n `6`; index avg `0.0093` n `26`; metal avg `0.0069` n `20`; unknown avg `0.0249` n `1108`
- 1h: commodity avg `0.0153` n `13`; crypto_alt avg `0.3316` n `235`; crypto_major avg `-0.0344` n `8`; equity avg `-0.0131` n `150`; fx avg `0.0033` n `6`; index avg `0.0049` n `26`; metal avg `0.0087` n `20`; unknown avg `0.052` n `1108`
- 4h: commodity avg `-0.0797` n `13`; crypto_alt avg `1.6351` n `235`; crypto_major avg `0.4938` n `8`; equity avg `0.0239` n `150`; fx avg `0.0046` n `6`; index avg `0.0128` n `26`; metal avg `0.0073` n `20`; unknown avg `0.4379` n `1046`
- 24h: commodity avg `-0.219` n `13`; crypto_alt avg `2.624` n `235`; crypto_major avg `0.4883` n `8`; equity avg `0.822` n `150`; fx avg `-0.0152` n `6`; index avg `0.1265` n `26`; metal avg `0.4502` n `20`; unknown avg `12.9869` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
