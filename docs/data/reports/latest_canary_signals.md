# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T13:37:32.322456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `13`; crypto_alt avg `0.1177` n `235`; crypto_major avg `0.034` n `8`; equity avg `0.0045` n `150`; fx avg `-0.0248` n `6`; index avg `-0.0027` n `26`; metal avg `0.0003` n `20`; unknown avg `0.174` n `1134`
- 1h: commodity avg `-0.0105` n `13`; crypto_alt avg `0.2609` n `235`; crypto_major avg `0.0349` n `8`; equity avg `0.0203` n `150`; fx avg `-0.0105` n `6`; index avg `-0.0066` n `26`; metal avg `0.0017` n `20`; unknown avg `0.2397` n `1059`
- 4h: commodity avg `-0.0353` n `13`; crypto_alt avg `0.2326` n `235`; crypto_major avg `0.1344` n `8`; equity avg `0.0999` n `150`; fx avg `0.0011` n `6`; index avg `-0.0062` n `26`; metal avg `0.007` n `20`; unknown avg `0.8388` n `1053`
- 24h: commodity avg `0.3132` n `13`; crypto_alt avg `1.2316` n `235`; crypto_major avg `0.013` n `8`; equity avg `0.1534` n `150`; fx avg `0.002` n `6`; index avg `-0.0019` n `26`; metal avg `0.0094` n `20`; unknown avg `0.7562` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
