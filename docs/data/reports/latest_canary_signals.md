# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T01:22:28.598183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0498` n `12`; crypto_alt avg `0.3229` n `234`; crypto_major avg `0.114` n `8`; equity avg `0.0337` n `142`; fx avg `-0.0463` n `6`; index avg `0.0036` n `26`; metal avg `-0.0381` n `20`; unknown avg `0.6235` n `963`
- 1h: commodity avg `0.0922` n `12`; crypto_alt avg `1.1906` n `234`; crypto_major avg `0.4347` n `8`; equity avg `-0.0517` n `142`; fx avg `-0.0079` n `6`; index avg `-0.0321` n `26`; metal avg `-0.0824` n `20`; unknown avg `1.3077` n `961`
- 4h: commodity avg `0.1346` n `12`; crypto_alt avg `0.285` n `234`; crypto_major avg `0.154` n `8`; equity avg `0.0244` n `142`; fx avg `0.0102` n `6`; index avg `0.0078` n `26`; metal avg `-0.0824` n `20`; unknown avg `0.6265` n `928`
- 24h: commodity avg `-0.8507` n `12`; crypto_alt avg `1.8971` n `234`; crypto_major avg `0.5745` n `8`; equity avg `1.2221` n `142`; fx avg `-0.1516` n `6`; index avg `0.1525` n `26`; metal avg `0.2195` n `20`; unknown avg `3100.9628` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
