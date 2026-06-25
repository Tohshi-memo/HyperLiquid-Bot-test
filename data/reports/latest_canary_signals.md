# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T18:22:38.048635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0564` n `12`; crypto_alt avg `-0.1651` n `228`; crypto_major avg `-0.2453` n `8`; equity avg `0.0384` n `86`; fx avg `-0.002` n `6`; index avg `0.0225` n `23`; metal avg `0.0988` n `20`; unknown avg `-0.0741` n `765`
- 1h: commodity avg `0.0586` n `12`; crypto_alt avg `-0.0954` n `228`; crypto_major avg `-0.0301` n `8`; equity avg `0.1994` n `86`; fx avg `0.0147` n `6`; index avg `0.0467` n `23`; metal avg `0.0084` n `20`; unknown avg `0.1435` n `765`
- 4h: commodity avg `0.186` n `12`; crypto_alt avg `0.4768` n `228`; crypto_major avg `0.8269` n `8`; equity avg `0.0615` n `86`; fx avg `0.0586` n `6`; index avg `0.0466` n `23`; metal avg `0.2425` n `20`; unknown avg `1.8893` n `765`
- 24h: commodity avg `0.4156` n `12`; crypto_alt avg `0.2552` n `228`; crypto_major avg `0.1231` n `8`; equity avg `0.053` n `86`; fx avg `0.0871` n `6`; index avg `0.4702` n `23`; metal avg `0.8202` n `20`; unknown avg `0.3664` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
