# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T21:22:30.292276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.0402` n `232`; crypto_major avg `-0.084` n `8`; equity avg `-0.0091` n `129`; fx avg `-0.0082` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0045` n `20`; unknown avg `-0.2039` n `793`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `-0.2967` n `232`; crypto_major avg `-0.4068` n `8`; equity avg `0.0042` n `129`; fx avg `0.0028` n `6`; index avg `0.0132` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.6768` n `785`
- 4h: commodity avg `0.0517` n `12`; crypto_alt avg `0.0878` n `232`; crypto_major avg `0.0813` n `8`; equity avg `0.3759` n `129`; fx avg `0.0043` n `6`; index avg `0.08` n `26`; metal avg `0.067` n `20`; unknown avg `-0.1326` n `773`
- 24h: commodity avg `0.1936` n `12`; crypto_alt avg `-0.1972` n `231`; crypto_major avg `-0.0393` n `8`; equity avg `0.0906` n `129`; fx avg `-0.0923` n `6`; index avg `-0.114` n `26`; metal avg `-0.4152` n `20`; unknown avg `-0.0433` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
