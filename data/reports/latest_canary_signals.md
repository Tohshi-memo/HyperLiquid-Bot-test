# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T06:22:28.668422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `0.0079` n `230`; crypto_major avg `0.0038` n `8`; equity avg `-0.0043` n `113`; fx avg `0.0178` n `6`; index avg `0.0058` n `25`; metal avg `-0.01` n `20`; unknown avg `0.0095` n `787`
- 1h: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.0199` n `230`; crypto_major avg `0.1035` n `8`; equity avg `-0.2749` n `113`; fx avg `0.0291` n `6`; index avg `-0.0452` n `25`; metal avg `-0.1729` n `20`; unknown avg `-0.0953` n `755`
- 4h: commodity avg `0.1694` n `12`; crypto_alt avg `0.4256` n `230`; crypto_major avg `0.796` n `8`; equity avg `-0.1585` n `113`; fx avg `0.0262` n `6`; index avg `-0.0357` n `25`; metal avg `-0.2286` n `20`; unknown avg `0.614` n `754`
- 24h: commodity avg `-0.1174` n `12`; crypto_alt avg `-0.7845` n `230`; crypto_major avg `0.4952` n `8`; equity avg `2.4873` n `113`; fx avg `-0.0283` n `6`; index avg `0.2867` n `25`; metal avg `-0.2287` n `20`; unknown avg `0.1418` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2453`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
