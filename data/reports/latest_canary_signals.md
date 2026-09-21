# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T03:37:28.571342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `0.0722` n `234`; crypto_major avg `-0.0169` n `8`; equity avg `-0.0441` n `140`; fx avg `0.0078` n `6`; index avg `-0.0078` n `26`; metal avg `0.0249` n `20`; unknown avg `-0.0646` n `944`
- 1h: commodity avg `-0.006` n `12`; crypto_alt avg `1.0658` n `234`; crypto_major avg `0.244` n `8`; equity avg `0.0898` n `140`; fx avg `-0.0188` n `6`; index avg `0.0184` n `26`; metal avg `-0.0236` n `20`; unknown avg `0.1099` n `942`
- 4h: commodity avg `-0.3911` n `12`; crypto_alt avg `0.7466` n `234`; crypto_major avg `0.4621` n `8`; equity avg `0.306` n `140`; fx avg `-0.0707` n `6`; index avg `0.0632` n `26`; metal avg `0.0066` n `20`; unknown avg `16.7582` n `935`
- 24h: commodity avg `-0.702` n `12`; crypto_alt avg `3.4594` n `234`; crypto_major avg `2.6736` n `8`; equity avg `1.0998` n `140`; fx avg `-0.0387` n `6`; index avg `0.201` n `26`; metal avg `0.0565` n `20`; unknown avg `4.1146` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
