# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T23:22:26.168338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.092` n `12`; crypto_alt avg `-0.3627` n `228`; crypto_major avg `-0.4573` n `8`; equity avg `-0.0821` n `88`; fx avg `0.0` n `6`; index avg `-0.0207` n `23`; metal avg `-0.025` n `20`; unknown avg `0.0516` n `764`
- 1h: commodity avg `-0.0304` n `12`; crypto_alt avg `0.0041` n `228`; crypto_major avg `-0.0225` n `8`; equity avg `-0.0216` n `88`; fx avg `0.005` n `6`; index avg `-0.0023` n `23`; metal avg `0.0141` n `20`; unknown avg `-0.7077` n `764`
- 4h: commodity avg `0.1393` n `12`; crypto_alt avg `-0.7973` n `228`; crypto_major avg `-0.8546` n `8`; equity avg `-0.1056` n `88`; fx avg `0.0108` n `6`; index avg `-0.0509` n `23`; metal avg `-0.0287` n `20`; unknown avg `-0.4824` n `764`
- 24h: commodity avg `0.1502` n `12`; crypto_alt avg `-0.8208` n `228`; crypto_major avg `-1.0636` n `8`; equity avg `0.2414` n `88`; fx avg `-0.0131` n `6`; index avg `-0.0552` n `23`; metal avg `-0.0733` n `20`; unknown avg `-1.0271` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2088`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
