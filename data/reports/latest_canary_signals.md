# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T20:07:28.535751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `13`; crypto_alt avg `0.1016` n `235`; crypto_major avg `0.0473` n `8`; equity avg `0.0676` n `150`; fx avg `0.0052` n `6`; index avg `0.0096` n `26`; metal avg `0.0119` n `20`; unknown avg `38.3255` n `1060`
- 1h: commodity avg `0.0692` n `13`; crypto_alt avg `-0.2399` n `235`; crypto_major avg `0.0007` n `8`; equity avg `-0.1316` n `150`; fx avg `0.0064` n `6`; index avg `-0.0344` n `26`; metal avg `-0.0686` n `20`; unknown avg `10.1349` n `1060`
- 4h: commodity avg `0.4306` n `13`; crypto_alt avg `-0.6371` n `235`; crypto_major avg `-0.5233` n `8`; equity avg `-0.2547` n `150`; fx avg `0.0035` n `6`; index avg `-0.1003` n `26`; metal avg `0.0314` n `20`; unknown avg `3.5089` n `1060`
- 24h: commodity avg `0.3021` n `13`; crypto_alt avg `-1.0437` n `235`; crypto_major avg `-0.7362` n `8`; equity avg `0.3339` n `149`; fx avg `0.1059` n `6`; index avg `-0.0253` n `26`; metal avg `0.0715` n `20`; unknown avg `5.2966` n `906`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
