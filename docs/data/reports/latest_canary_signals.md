# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T10:07:30.828229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `10`; crypto_alt avg `-0.0413` n `232`; crypto_major avg `-0.002` n `7`; equity avg `-0.115` n `132`; fx avg `0.0014` n `6`; index avg `-0.0019` n `23`; metal avg `0.0203` n `13`; unknown avg `0.8179` n `898`
- 1h: commodity avg `-0.067` n `10`; crypto_alt avg `0.2138` n `232`; crypto_major avg `0.2423` n `7`; equity avg `-0.0314` n `132`; fx avg `-0.0101` n `6`; index avg `-0.012` n `23`; metal avg `0.0378` n `13`; unknown avg `0.3336` n `898`
- 4h: commodity avg `-0.0459` n `10`; crypto_alt avg `-0.1994` n `232`; crypto_major avg `-0.0748` n `7`; equity avg `0.1078` n `132`; fx avg `-0.0355` n `6`; index avg `0.0454` n `23`; metal avg `0.0319` n `13`; unknown avg `6.3855` n `892`
- 24h: commodity avg `0.1281` n `10`; crypto_alt avg `-2.9587` n `232`; crypto_major avg `-3.1124` n `7`; equity avg `-0.0874` n `132`; fx avg `0.116` n `6`; index avg `0.1262` n `23`; metal avg `0.7259` n `13`; unknown avg `19328.4341` n `780`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
