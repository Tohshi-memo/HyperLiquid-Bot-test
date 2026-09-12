# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T07:37:28.143652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.65` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.0121` n `233`; crypto_major avg `-0.0238` n `8`; equity avg `-0.0033` n `136`; fx avg `-0.0033` n `6`; index avg `0.0022` n `26`; metal avg `0.0008` n `20`; unknown avg `-0.1016` n `840`
- 1h: commodity avg `-0.0131` n `12`; crypto_alt avg `0.323` n `233`; crypto_major avg `0.1452` n `8`; equity avg `-0.0051` n `136`; fx avg `0.0003` n `6`; index avg `0.0028` n `26`; metal avg `-0.0015` n `20`; unknown avg `-0.2427` n `836`
- 4h: commodity avg `-0.0957` n `12`; crypto_alt avg `0.5043` n `233`; crypto_major avg `0.1191` n `8`; equity avg `-0.0855` n `136`; fx avg `-0.0001` n `6`; index avg `0.0074` n `26`; metal avg `0.0068` n `20`; unknown avg `1.9119` n `796`
- 24h: commodity avg `-0.435` n `12`; crypto_alt avg `1.2924` n `233`; crypto_major avg `0.8628` n `8`; equity avg `0.2422` n `136`; fx avg `-0.1236` n `6`; index avg `0.1775` n `26`; metal avg `-0.0166` n `20`; unknown avg `0.7872` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
