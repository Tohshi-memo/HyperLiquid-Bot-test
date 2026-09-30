# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T02:52:25.398751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0287` n `12`; crypto_alt avg `0.266` n `234`; crypto_major avg `0.2128` n `8`; equity avg `0.1462` n `142`; fx avg `0.0188` n `6`; index avg `0.0346` n `26`; metal avg `0.0674` n `20`; unknown avg `2.98` n `963`
- 1h: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.2476` n `234`; crypto_major avg `0.039` n `8`; equity avg `-0.1033` n `142`; fx avg `-0.0419` n `6`; index avg `-0.0173` n `26`; metal avg `0.0912` n `20`; unknown avg `1.672` n `961`
- 4h: commodity avg `0.0396` n `12`; crypto_alt avg `0.2996` n `234`; crypto_major avg `0.0914` n `8`; equity avg `-0.2349` n `142`; fx avg `-0.05` n `6`; index avg `-0.0493` n `26`; metal avg `-0.0398` n `20`; unknown avg `0.3935` n `955`
- 24h: commodity avg `-0.9618` n `12`; crypto_alt avg `3.1071` n `234`; crypto_major avg `1.1991` n `8`; equity avg `1.0231` n `142`; fx avg `-0.1921` n `6`; index avg `0.1454` n `26`; metal avg `0.2429` n `20`; unknown avg `3230.6679` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
