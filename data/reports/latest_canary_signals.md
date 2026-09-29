# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T18:52:33.967337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0914` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `0.2791` n `234`; crypto_major avg `0.1652` n `8`; equity avg `0.1533` n `142`; fx avg `-0.0066` n `6`; index avg `0.0389` n `26`; metal avg `0.0188` n `20`; unknown avg `1.817` n `962`
- 1h: commodity avg `-0.1881` n `12`; crypto_alt avg `1.3913` n `234`; crypto_major avg `0.9306` n `8`; equity avg `0.316` n `142`; fx avg `0.0084` n `6`; index avg `0.0921` n `26`; metal avg `0.2205` n `20`; unknown avg `4.965` n `960`
- 4h: commodity avg `-0.3044` n `12`; crypto_alt avg `-1.4864` n `234`; crypto_major avg `-1.1287` n `8`; equity avg `-0.4723` n `142`; fx avg `-0.0416` n `6`; index avg `-0.0373` n `26`; metal avg `0.0907` n `20`; unknown avg `10.872` n `924`
- 24h: commodity avg `-0.6577` n `12`; crypto_alt avg `0.2731` n `234`; crypto_major avg `-0.9238` n `8`; equity avg `0.3467` n `142`; fx avg `-0.1661` n `6`; index avg `0.0211` n `26`; metal avg `0.0293` n `20`; unknown avg `2.1282` n `786`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
