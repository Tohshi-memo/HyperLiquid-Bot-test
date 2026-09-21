# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T22:07:30.374898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0579` n `12`; crypto_alt avg `0.1287` n `234`; crypto_major avg `0.2363` n `8`; equity avg `0.0502` n `140`; fx avg `-0.0084` n `6`; index avg `0.0283` n `26`; metal avg `0.0624` n `20`; unknown avg `-0.0662` n `942`
- 1h: commodity avg `-0.0732` n `12`; crypto_alt avg `0.1092` n `234`; crypto_major avg `0.4228` n `8`; equity avg `0.1101` n `140`; fx avg `-0.0061` n `6`; index avg `0.0044` n `26`; metal avg `0.0269` n `20`; unknown avg `-0.2269` n `942`
- 4h: commodity avg `-0.1367` n `12`; crypto_alt avg `0.5507` n `234`; crypto_major avg `1.2595` n `8`; equity avg `0.187` n `140`; fx avg `-0.0002` n `6`; index avg `0.0298` n `26`; metal avg `0.0524` n `20`; unknown avg `0.4431` n `852`
- 24h: commodity avg `-0.8881` n `12`; crypto_alt avg `3.5073` n `234`; crypto_major avg `6.2659` n `8`; equity avg `2.7954` n `140`; fx avg `-0.1092` n `6`; index avg `0.6097` n `26`; metal avg `0.0172` n `20`; unknown avg `7.8263` n `755`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
