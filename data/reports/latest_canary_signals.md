# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T21:22:28.358624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.0919` n `234`; crypto_major avg `-0.064` n `8`; equity avg `0.0176` n `140`; fx avg `-0.004` n `6`; index avg `-0.0192` n `26`; metal avg `-0.0208` n `20`; unknown avg `0.0301` n `944`
- 1h: commodity avg `0.0341` n `12`; crypto_alt avg `-0.346` n `234`; crypto_major avg `-0.5036` n `8`; equity avg `0.0435` n `140`; fx avg `-0.0035` n `6`; index avg `-0.0014` n `26`; metal avg `-0.0037` n `20`; unknown avg `71.0915` n `920`
- 4h: commodity avg `0.0584` n `12`; crypto_alt avg `0.5206` n `234`; crypto_major avg `0.985` n `8`; equity avg `0.2907` n `140`; fx avg `0.0043` n `6`; index avg `0.0302` n `26`; metal avg `0.0429` n `20`; unknown avg `31.3415` n `852`
- 24h: commodity avg `-1.0246` n `12`; crypto_alt avg `4.1176` n `234`; crypto_major avg `6.1747` n `8`; equity avg `2.8586` n `140`; fx avg `-0.0556` n `6`; index avg `0.5965` n `26`; metal avg `0.059` n `20`; unknown avg `12.5492` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
