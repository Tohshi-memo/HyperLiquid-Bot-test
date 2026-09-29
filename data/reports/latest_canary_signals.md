# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T20:22:31.297889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `0.2179` n `234`; crypto_major avg `0.1453` n `8`; equity avg `0.0332` n `142`; fx avg `-0.0017` n `6`; index avg `0.0054` n `26`; metal avg `-0.0059` n `20`; unknown avg `-0.1702` n `934`
- 1h: commodity avg `-0.061` n `12`; crypto_alt avg `-0.0604` n `234`; crypto_major avg `-0.1533` n `8`; equity avg `-0.0188` n `142`; fx avg `-0.0017` n `6`; index avg `0.0022` n `26`; metal avg `0.0181` n `20`; unknown avg `310.0068` n `924`
- 4h: commodity avg `-0.3026` n `12`; crypto_alt avg `-0.1874` n `234`; crypto_major avg `-0.1869` n `8`; equity avg `-0.0139` n `142`; fx avg `0.0049` n `6`; index avg `0.075` n `26`; metal avg `0.2535` n `20`; unknown avg `12.2781` n `924`
- 24h: commodity avg `-0.8948` n `12`; crypto_alt avg `0.9202` n `234`; crypto_major avg `-0.3331` n `8`; equity avg `0.7245` n `142`; fx avg `-0.171` n `6`; index avg `0.0811` n `26`; metal avg `0.1868` n `20`; unknown avg `-0.4615` n `814`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.2007`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1972`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
