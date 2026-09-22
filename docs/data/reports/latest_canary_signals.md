# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T11:22:32.733822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.068` n `12`; crypto_alt avg `0.3898` n `234`; crypto_major avg `0.2872` n `8`; equity avg `-0.1226` n `140`; fx avg `-0.0036` n `6`; index avg `-0.0244` n `26`; metal avg `-0.0421` n `20`; unknown avg `0.139` n `944`
- 1h: commodity avg `0.1086` n `12`; crypto_alt avg `0.0185` n `234`; crypto_major avg `0.0793` n `8`; equity avg `-0.074` n `140`; fx avg `0.0006` n `6`; index avg `-0.0165` n `26`; metal avg `-0.0452` n `20`; unknown avg `0.9631` n `942`
- 4h: commodity avg `-0.492` n `12`; crypto_alt avg `-0.1586` n `234`; crypto_major avg `0.4973` n `8`; equity avg `0.3155` n `140`; fx avg `-0.1279` n `6`; index avg `0.046` n `26`; metal avg `0.0028` n `20`; unknown avg `1.4759` n `934`
- 24h: commodity avg `-0.4947` n `12`; crypto_alt avg `-0.0702` n `234`; crypto_major avg `1.2295` n `8`; equity avg `0.9788` n `140`; fx avg `-0.2799` n `6`; index avg `0.244` n `26`; metal avg `-0.1818` n `20`; unknown avg `1123.4648` n `790`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
