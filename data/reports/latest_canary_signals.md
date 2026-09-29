# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T21:22:34.365622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0353` n `12`; crypto_alt avg `-0.1209` n `234`; crypto_major avg `-0.1318` n `8`; equity avg `0.0151` n `142`; fx avg `-0.0145` n `6`; index avg `0.0056` n `26`; metal avg `-0.0015` n `20`; unknown avg `2.6776` n `960`
- 1h: commodity avg `0.018` n `12`; crypto_alt avg `-0.1117` n `234`; crypto_major avg `-0.1103` n `8`; equity avg `0.072` n `142`; fx avg `-0.0105` n `6`; index avg `0.0048` n `26`; metal avg `0.0472` n `20`; unknown avg `2.4169` n `932`
- 4h: commodity avg `-0.2795` n `12`; crypto_alt avg `0.9626` n `234`; crypto_major avg `0.5602` n `8`; equity avg `0.2674` n `142`; fx avg `-0.0002` n `6`; index avg `0.109` n `26`; metal avg `0.2977` n `20`; unknown avg `2.2554` n `896`
- 24h: commodity avg `-0.9192` n `12`; crypto_alt avg `1.0025` n `234`; crypto_major avg `-0.2163` n `8`; equity avg `0.6989` n `142`; fx avg `-0.1858` n `6`; index avg `0.0649` n `26`; metal avg `0.2727` n `20`; unknown avg `3099.1514` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1961`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.193`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
