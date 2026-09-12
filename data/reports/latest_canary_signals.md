# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T01:07:25.624273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `0.1134` n `233`; crypto_major avg `0.1257` n `8`; equity avg `0.0044` n `136`; fx avg `0.0147` n `6`; index avg `0.0` n `26`; metal avg `-0.0027` n `20`; unknown avg `9.2857` n `834`
- 1h: commodity avg `-0.0214` n `12`; crypto_alt avg `0.4294` n `233`; crypto_major avg `0.0702` n `8`; equity avg `0.0258` n `136`; fx avg `0.0143` n `6`; index avg `0.0149` n `26`; metal avg `0.0058` n `20`; unknown avg `0.3669` n `828`
- 4h: commodity avg `-0.0538` n `12`; crypto_alt avg `0.1438` n `233`; crypto_major avg `-0.4977` n `8`; equity avg `0.0589` n `136`; fx avg `-0.0081` n `6`; index avg `0.0466` n `26`; metal avg `-0.0317` n `20`; unknown avg `3.1071` n `814`
- 24h: commodity avg `-0.5582` n `12`; crypto_alt avg `0.919` n `233`; crypto_major avg `1.083` n `8`; equity avg `0.6817` n `136`; fx avg `-0.1539` n `6`; index avg `0.2855` n `26`; metal avg `0.1738` n `20`; unknown avg `1.6414` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
