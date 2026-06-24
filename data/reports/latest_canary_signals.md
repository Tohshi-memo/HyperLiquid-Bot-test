# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T08:37:35.017165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0375` n `12`; crypto_alt avg `0.0487` n `228`; crypto_major avg `0.1416` n `8`; equity avg `-0.04` n `86`; fx avg `-0.0051` n `6`; index avg `0.0137` n `23`; metal avg `0.0307` n `20`; unknown avg `0.017` n `764`
- 1h: commodity avg `-0.0603` n `12`; crypto_alt avg `0.1538` n `228`; crypto_major avg `0.1839` n `8`; equity avg `0.1704` n `86`; fx avg `-0.0197` n `6`; index avg `0.0579` n `23`; metal avg `-0.0324` n `20`; unknown avg `0.0268` n `764`
- 4h: commodity avg `-0.0906` n `12`; crypto_alt avg `0.462` n `228`; crypto_major avg `0.3695` n `8`; equity avg `0.6244` n `86`; fx avg `0.0383` n `6`; index avg `0.193` n `23`; metal avg `0.1264` n `20`; unknown avg `-0.0019` n `740`
- 24h: commodity avg `-0.5824` n `12`; crypto_alt avg `0.7009` n `228`; crypto_major avg `0.2861` n `8`; equity avg `5.2285` n `86`; fx avg `-0.0345` n `6`; index avg `0.1322` n `23`; metal avg `-0.2118` n `20`; unknown avg `0.13` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
