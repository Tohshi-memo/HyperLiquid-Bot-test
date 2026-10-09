# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T23:52:27.659308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `13`; crypto_alt avg `0.1725` n `235`; crypto_major avg `0.0629` n `8`; equity avg `0.0122` n `150`; fx avg `-0.0005` n `6`; index avg `-0.004` n `26`; metal avg `0.0085` n `20`; unknown avg `0.1196` n `1116`
- 1h: commodity avg `0.0504` n `13`; crypto_alt avg `0.4851` n `235`; crypto_major avg `0.0284` n `8`; equity avg `0.0022` n `150`; fx avg `0.0001` n `6`; index avg `-0.0025` n `26`; metal avg `0.0049` n `20`; unknown avg `0.0352` n `1114`
- 4h: commodity avg `-0.0` n `13`; crypto_alt avg `1.87` n `235`; crypto_major avg `0.7131` n `8`; equity avg `0.1343` n `150`; fx avg `0.0067` n `6`; index avg `0.0137` n `26`; metal avg `0.0121` n `20`; unknown avg `0.6046` n `1026`
- 24h: commodity avg `-0.2227` n `13`; crypto_alt avg `2.8215` n `235`; crypto_major avg `0.724` n `8`; equity avg `1.0002` n `150`; fx avg `-0.0222` n `6`; index avg `0.1477` n `26`; metal avg `0.4831` n `20`; unknown avg `12.9732` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
