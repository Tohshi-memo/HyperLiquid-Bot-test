# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T08:22:27.938226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `0.3761` n `234`; crypto_major avg `0.2718` n `8`; equity avg `0.0386` n `140`; fx avg `-0.0033` n `6`; index avg `0.0078` n `26`; metal avg `0.006` n `20`; unknown avg `0.0647` n `942`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `0.511` n `234`; crypto_major avg `0.2292` n `8`; equity avg `0.0236` n `140`; fx avg `-0.0144` n `6`; index avg `-0.0309` n `26`; metal avg `-0.0055` n `20`; unknown avg `0.0196` n `934`
- 4h: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.2862` n `234`; crypto_major avg `-0.1502` n `8`; equity avg `-0.0631` n `140`; fx avg `-0.0013` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0081` n `20`; unknown avg `0.4064` n `898`
- 24h: commodity avg `0.243` n `12`; crypto_alt avg `3.3765` n `234`; crypto_major avg `4.0281` n `8`; equity avg `0.0326` n `140`; fx avg `-0.0295` n `6`; index avg `-0.096` n `26`; metal avg `-0.2432` n `20`; unknown avg `2.3257` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
