# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T08:37:27.215309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `0.1915` n `235`; crypto_major avg `0.05` n `8`; equity avg `0.0025` n `150`; fx avg `-0.0038` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0013` n `20`; unknown avg `-0.08` n `1117`
- 1h: commodity avg `0.0193` n `13`; crypto_alt avg `0.1739` n `235`; crypto_major avg `0.0717` n `8`; equity avg `0.0` n `150`; fx avg `-0.001` n `6`; index avg `0.0008` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.0572` n `1099`
- 4h: commodity avg `0.0115` n `13`; crypto_alt avg `0.737` n `235`; crypto_major avg `-0.0503` n `8`; equity avg `0.0134` n `150`; fx avg `-0.0` n `6`; index avg `0.0037` n `26`; metal avg `0.0133` n `20`; unknown avg `0.4132` n `1083`
- 24h: commodity avg `0.1914` n `13`; crypto_alt avg `1.3205` n `235`; crypto_major avg `-0.1677` n `8`; equity avg `0.0645` n `150`; fx avg `-0.0183` n `6`; index avg `0.0059` n `26`; metal avg `0.0107` n `20`; unknown avg `0.4881` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
