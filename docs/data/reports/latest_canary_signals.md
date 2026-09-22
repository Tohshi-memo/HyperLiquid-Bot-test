# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T07:22:31.705354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `12`; crypto_alt avg `-0.1441` n `234`; crypto_major avg `-0.2698` n `8`; equity avg `0.0539` n `140`; fx avg `0.0228` n `6`; index avg `-0.0007` n `26`; metal avg `0.0388` n `20`; unknown avg `-0.1572` n `944`
- 1h: commodity avg `-0.0824` n `12`; crypto_alt avg `0.2023` n `234`; crypto_major avg `0.0078` n `8`; equity avg `0.0855` n `140`; fx avg `0.0384` n `6`; index avg `-0.0109` n `26`; metal avg `0.0514` n `20`; unknown avg `0.1191` n `942`
- 4h: commodity avg `0.0152` n `12`; crypto_alt avg `0.3203` n `234`; crypto_major avg `0.1705` n `8`; equity avg `-0.8647` n `140`; fx avg `0.0144` n `6`; index avg `-0.1243` n `26`; metal avg `-0.135` n `20`; unknown avg `7.9968` n `908`
- 24h: commodity avg `-0.1273` n `12`; crypto_alt avg `2.657` n `234`; crypto_major avg `3.6074` n `8`; equity avg `1.2807` n `140`; fx avg `-0.19` n `6`; index avg `0.2912` n `26`; metal avg `-0.1434` n `20`; unknown avg `1123.4964` n `792`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
