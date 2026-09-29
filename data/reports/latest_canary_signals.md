# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T21:07:36.245145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `-0.0494` n `234`; crypto_major avg `-0.0475` n `8`; equity avg `0.0044` n `142`; fx avg `0.0028` n `6`; index avg `-0.0162` n `26`; metal avg `0.0108` n `20`; unknown avg `0.7927` n `954`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.2273` n `234`; crypto_major avg `0.167` n `8`; equity avg `0.0901` n `142`; fx avg `0.0023` n `6`; index avg `0.0046` n `26`; metal avg `0.0427` n `20`; unknown avg `1.5904` n `904`
- 4h: commodity avg `-0.3306` n `12`; crypto_alt avg `0.6289` n `234`; crypto_major avg `0.3822` n `8`; equity avg `0.2451` n `142`; fx avg `0.0142` n `6`; index avg `0.1107` n `26`; metal avg `0.3358` n `20`; unknown avg `2.0116` n `896`
- 24h: commodity avg `-0.981` n `12`; crypto_alt avg `0.8688` n `234`; crypto_major avg `-0.3045` n `8`; equity avg `0.728` n `142`; fx avg `-0.1727` n `6`; index avg `0.0684` n `26`; metal avg `0.2896` n `20`; unknown avg `3099.1285` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1971`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1939`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
