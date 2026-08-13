# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T21:22:48.798219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `0.1279` n `230`; crypto_major avg `-0.0381` n `8`; equity avg `0.0882` n `113`; fx avg `0.0016` n `6`; index avg `0.0068` n `25`; metal avg `0.0184` n `20`; unknown avg `0.0193` n `787`
- 1h: commodity avg `0.0167` n `12`; crypto_alt avg `0.158` n `230`; crypto_major avg `0.0035` n `8`; equity avg `0.1549` n `113`; fx avg `-0.0019` n `6`; index avg `0.022` n `25`; metal avg `0.028` n `20`; unknown avg `-0.103` n `787`
- 4h: commodity avg `-0.1565` n `12`; crypto_alt avg `0.2792` n `230`; crypto_major avg `0.3129` n `8`; equity avg `-0.1293` n `113`; fx avg `0.0067` n `6`; index avg `-0.0262` n `25`; metal avg `-0.1135` n `20`; unknown avg `-0.0124` n `787`
- 24h: commodity avg `-0.4769` n `12`; crypto_alt avg `-0.1315` n `230`; crypto_major avg `0.3062` n `8`; equity avg `1.5985` n `113`; fx avg `0.0252` n `6`; index avg `0.3218` n `25`; metal avg `-0.4615` n `20`; unknown avg `0.0389` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2419`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
