# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T08:52:26.074088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `13`; crypto_alt avg `0.1463` n `235`; crypto_major avg `0.0348` n `8`; equity avg `0.0039` n `150`; fx avg `-0.0176` n `6`; index avg `0.0045` n `26`; metal avg `0.0074` n `20`; unknown avg `0.067` n `1117`
- 1h: commodity avg `-0.0216` n `13`; crypto_alt avg `0.2666` n `235`; crypto_major avg `0.1101` n `8`; equity avg `0.0104` n `150`; fx avg `-0.0122` n `6`; index avg `-0.0008` n `26`; metal avg `0.0034` n `20`; unknown avg `0.5188` n `1099`
- 4h: commodity avg `-0.001` n `13`; crypto_alt avg `-0.0645` n `235`; crypto_major avg `0.1808` n `8`; equity avg `-0.09` n `150`; fx avg `-0.0112` n `6`; index avg `-0.035` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.8342` n `1082`
- 24h: commodity avg `0.1503` n `13`; crypto_alt avg `1.3064` n `235`; crypto_major avg `0.0739` n `8`; equity avg `-0.3574` n `150`; fx avg `-0.0496` n `6`; index avg `-0.0666` n `26`; metal avg `0.0631` n `20`; unknown avg `632.7723` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
