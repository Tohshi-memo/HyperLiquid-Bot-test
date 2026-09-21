# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T02:22:26.945130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.3897` n `234`; crypto_major avg `0.4034` n `8`; equity avg `-0.0056` n `140`; fx avg `-0.0201` n `6`; index avg `0.0014` n `26`; metal avg `-0.0632` n `20`; unknown avg `-0.2681` n `944`
- 1h: commodity avg `0.0565` n `12`; crypto_alt avg `-1.3055` n `234`; crypto_major avg `-0.9398` n `8`; equity avg `-0.2167` n `140`; fx avg `0.0063` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0682` n `20`; unknown avg `3.009` n `942`
- 4h: commodity avg `-0.4465` n `12`; crypto_alt avg `-0.2159` n `234`; crypto_major avg `0.7744` n `8`; equity avg `0.5389` n `140`; fx avg `-0.0576` n `6`; index avg `0.0876` n `26`; metal avg `-0.0047` n `20`; unknown avg `17.8446` n `935`
- 24h: commodity avg `-0.5426` n `12`; crypto_alt avg `0.682` n `234`; crypto_major avg `1.4029` n `8`; equity avg `0.5913` n `140`; fx avg `-0.0242` n `6`; index avg `0.1032` n `26`; metal avg `0.017` n `20`; unknown avg `2.9767` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
