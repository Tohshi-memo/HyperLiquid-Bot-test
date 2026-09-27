# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T01:07:30.318829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `-0.0081` n `234`; crypto_major avg `-0.0019` n `8`; equity avg `-0.015` n `141`; fx avg `-0.0014` n `6`; index avg `0.0007` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.0841` n `959`
- 1h: commodity avg `-0.0642` n `12`; crypto_alt avg `-0.2253` n `234`; crypto_major avg `-0.1179` n `8`; equity avg `-0.0045` n `141`; fx avg `0.0035` n `6`; index avg `-0.007` n `26`; metal avg `-0.002` n `20`; unknown avg `13.8176` n `957`
- 4h: commodity avg `-0.0715` n `12`; crypto_alt avg `0.3725` n `234`; crypto_major avg `0.3349` n `8`; equity avg `0.0969` n `141`; fx avg `0.0023` n `6`; index avg `0.0063` n `26`; metal avg `0.0017` n `20`; unknown avg `0.2179` n `927`
- 24h: commodity avg `-0.1374` n `12`; crypto_alt avg `0.574` n `234`; crypto_major avg `-0.6695` n `8`; equity avg `0.2283` n `141`; fx avg `0.021` n `6`; index avg `0.0057` n `26`; metal avg `-0.0041` n `20`; unknown avg `4.4068` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
