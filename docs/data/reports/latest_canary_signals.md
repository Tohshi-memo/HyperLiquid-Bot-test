# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T00:52:30.001943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `13`; crypto_alt avg `-0.1582` n `235`; crypto_major avg `-0.0527` n `8`; equity avg `-0.0017` n `150`; fx avg `0.0` n `6`; index avg `0.001` n `26`; metal avg `0.0016` n `20`; unknown avg `1.9207` n `1117`
- 1h: commodity avg `0.0119` n `13`; crypto_alt avg `-0.3733` n `235`; crypto_major avg `-0.2281` n `8`; equity avg `-0.0255` n `150`; fx avg `0.0003` n `6`; index avg `0.0015` n `26`; metal avg `-0.0007` n `20`; unknown avg `1.2535` n `1109`
- 4h: commodity avg `0.2157` n `13`; crypto_alt avg `-0.6181` n `235`; crypto_major avg `-0.3792` n `8`; equity avg `-0.0252` n `150`; fx avg `0.0007` n `6`; index avg `-0.0004` n `26`; metal avg `0.0115` n `20`; unknown avg `3.582` n `1079`
- 24h: commodity avg `0.0867` n `13`; crypto_alt avg `1.0675` n `235`; crypto_major avg `0.333` n `8`; equity avg `0.0771` n `150`; fx avg `-0.0114` n `6`; index avg `-0.0063` n `26`; metal avg `-0.0206` n `20`; unknown avg `0.344` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
