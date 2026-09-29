# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T11:52:38.222479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0943` n `12`; crypto_alt avg `0.4169` n `234`; crypto_major avg `0.3076` n `8`; equity avg `0.0854` n `141`; fx avg `-0.0075` n `6`; index avg `0.0145` n `26`; metal avg `0.0124` n `20`; unknown avg `206.0312` n `963`
- 1h: commodity avg `-0.0711` n `12`; crypto_alt avg `0.857` n `234`; crypto_major avg `0.5387` n `8`; equity avg `0.2012` n `141`; fx avg `-0.0027` n `6`; index avg `0.0539` n `26`; metal avg `0.1271` n `20`; unknown avg `210.812` n `961`
- 4h: commodity avg `-0.3942` n `12`; crypto_alt avg `1.2874` n `234`; crypto_major avg `0.4862` n `8`; equity avg `0.4618` n `141`; fx avg `-0.0378` n `6`; index avg `0.071` n `26`; metal avg `0.1941` n `20`; unknown avg `183.6131` n `945`
- 24h: commodity avg `-0.8433` n `12`; crypto_alt avg `2.2678` n `234`; crypto_major avg `1.2378` n `8`; equity avg `0.0271` n `141`; fx avg `-0.0953` n `6`; index avg `0.0215` n `26`; metal avg `-0.0462` n `20`; unknown avg `77.8565` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
