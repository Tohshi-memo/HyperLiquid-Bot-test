# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T13:22:25.660651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.1018` n `234`; crypto_major avg `0.0543` n `8`; equity avg `0.0014` n `140`; fx avg `-0.005` n `6`; index avg `0.0002` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.2923` n `942`
- 1h: commodity avg `0.0165` n `12`; crypto_alt avg `-0.2114` n `234`; crypto_major avg `0.1994` n `8`; equity avg `0.0` n `140`; fx avg `-0.0058` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0028` n `20`; unknown avg `-0.1688` n `940`
- 4h: commodity avg `0.0145` n `12`; crypto_alt avg `0.6262` n `234`; crypto_major avg `0.2975` n `8`; equity avg `0.0214` n `140`; fx avg `-0.0323` n `6`; index avg `-0.0014` n `26`; metal avg `0.0179` n `20`; unknown avg `0.3595` n `934`
- 24h: commodity avg `-0.0766` n `12`; crypto_alt avg `3.7192` n `234`; crypto_major avg `3.919` n `8`; equity avg `0.6574` n `140`; fx avg `-0.0206` n `6`; index avg `0.0526` n `26`; metal avg `-0.0445` n `20`; unknown avg `2.2485` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
