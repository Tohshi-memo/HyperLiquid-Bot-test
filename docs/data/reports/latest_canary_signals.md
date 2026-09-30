# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T00:07:27.993165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0484` n `12`; crypto_alt avg `0.1004` n `234`; crypto_major avg `-0.0078` n `8`; equity avg `0.1041` n `142`; fx avg `0.0042` n `6`; index avg `0.0095` n `26`; metal avg `-0.0165` n `20`; unknown avg `0.4755` n `955`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `-0.724` n `234`; crypto_major avg `-0.3567` n `8`; equity avg `0.152` n `142`; fx avg `-0.0087` n `6`; index avg `0.0383` n `26`; metal avg `0.0114` n `20`; unknown avg `2.3119` n `955`
- 4h: commodity avg `0.1119` n `12`; crypto_alt avg `-0.3152` n `234`; crypto_major avg `0.0888` n `8`; equity avg `0.3232` n `142`; fx avg `-0.0094` n `6`; index avg `0.0689` n `26`; metal avg `0.0712` n `20`; unknown avg `4.5942` n `874`
- 24h: commodity avg `-0.8755` n `12`; crypto_alt avg `-0.2562` n `234`; crypto_major avg `-0.3822` n `8`; equity avg `0.8372` n `142`; fx avg `-0.1611` n `6`; index avg `0.1133` n `26`; metal avg `0.2742` n `20`; unknown avg `3099.2223` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1824`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
