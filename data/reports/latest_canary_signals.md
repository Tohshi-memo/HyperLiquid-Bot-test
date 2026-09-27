# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T01:22:29.334374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `74.54` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.0003` n `234`; crypto_major avg `0.0805` n `8`; equity avg `0.016` n `141`; fx avg `0.0014` n `6`; index avg `0.0019` n `26`; metal avg `-0.0001` n `20`; unknown avg `-0.1626` n `961`
- 1h: commodity avg `-0.0448` n `12`; crypto_alt avg `-0.1209` n `234`; crypto_major avg `0.0675` n `8`; equity avg `-0.0083` n `141`; fx avg `-0.0001` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0056` n `20`; unknown avg `7.0719` n `957`
- 4h: commodity avg `-0.081` n `12`; crypto_alt avg `0.1366` n `234`; crypto_major avg `0.2539` n `8`; equity avg `0.1067` n `141`; fx avg `-0.0017` n `6`; index avg `0.0083` n `26`; metal avg `-0.0` n `20`; unknown avg `0.1527` n `927`
- 24h: commodity avg `-0.1166` n `12`; crypto_alt avg `0.3302` n `234`; crypto_major avg `-0.734` n `8`; equity avg `0.2432` n `141`; fx avg `0.0214` n `6`; index avg `0.0106` n `26`; metal avg `0.004` n `20`; unknown avg `4.133` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
