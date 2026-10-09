# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T23:22:26.113057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `0.1362` n `235`; crypto_major avg `0.0732` n `8`; equity avg `0.001` n `150`; fx avg `-0.001` n `6`; index avg `-0.0004` n `26`; metal avg `0.0013` n `20`; unknown avg `0.025` n `1116`
- 1h: commodity avg `0.099` n `13`; crypto_alt avg `0.6017` n `235`; crypto_major avg `0.1445` n `8`; equity avg `0.0192` n `150`; fx avg `0.0014` n `6`; index avg `0.0123` n `26`; metal avg `0.0076` n `20`; unknown avg `0.1411` n `1114`
- 4h: commodity avg `-0.0269` n `13`; crypto_alt avg `1.0137` n `235`; crypto_major avg `0.2431` n `8`; equity avg `-0.0504` n `150`; fx avg `-0.0027` n `6`; index avg `-0.0135` n `26`; metal avg `-0.0157` n `20`; unknown avg `0.2845` n `1026`
- 24h: commodity avg `-0.1419` n `13`; crypto_alt avg `2.0025` n `235`; crypto_major avg `0.2838` n `8`; equity avg `0.7929` n `150`; fx avg `0.0032` n `6`; index avg `0.1269` n `26`; metal avg `0.5077` n `20`; unknown avg `12.7797` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
