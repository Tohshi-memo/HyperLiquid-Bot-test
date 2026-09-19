# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T07:37:29.221591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.1808` n `234`; crypto_major avg `-0.1502` n `8`; equity avg `-0.0263` n `140`; fx avg `-0.0109` n `6`; index avg `-0.0163` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.7654` n `942`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.11` n `234`; crypto_major avg `-0.2428` n `8`; equity avg `-0.0069` n `140`; fx avg `0.008` n `6`; index avg `0.0316` n `26`; metal avg `0.0017` n `20`; unknown avg `0.0316` n `940`
- 4h: commodity avg `-0.0372` n `12`; crypto_alt avg `-0.995` n `234`; crypto_major avg `-0.3909` n `8`; equity avg `-0.0907` n `140`; fx avg `-0.0049` n `6`; index avg `-0.0196` n `26`; metal avg `-0.0016` n `20`; unknown avg `43.5413` n `896`
- 24h: commodity avg `0.3569` n `12`; crypto_alt avg `2.7845` n `234`; crypto_major avg `3.8802` n `8`; equity avg `-0.0053` n `140`; fx avg `0.0386` n `6`; index avg `-0.0847` n `26`; metal avg `-0.2659` n `20`; unknown avg `2.0657` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
