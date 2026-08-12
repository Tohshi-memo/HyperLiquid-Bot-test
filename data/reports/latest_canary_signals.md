# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T08:07:36.836804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0281` n `12`; crypto_alt avg `0.0866` n `230`; crypto_major avg `0.1257` n `8`; equity avg `0.1417` n `113`; fx avg `-0.008` n `6`; index avg `0.0281` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.0278` n `786`
- 1h: commodity avg `0.0218` n `12`; crypto_alt avg `-0.0686` n `230`; crypto_major avg `0.0533` n `8`; equity avg `0.2141` n `113`; fx avg `-0.0173` n `6`; index avg `0.0188` n `25`; metal avg `0.0635` n `20`; unknown avg `-0.0114` n `786`
- 4h: commodity avg `-0.048` n `12`; crypto_alt avg `-0.4913` n `230`; crypto_major avg `0.0222` n `8`; equity avg `0.2125` n `113`; fx avg `0.0106` n `6`; index avg `0.0187` n `25`; metal avg `0.1315` n `20`; unknown avg `-0.0521` n `770`
- 24h: commodity avg `-0.0663` n `12`; crypto_alt avg `-0.9812` n `230`; crypto_major avg `0.8087` n `8`; equity avg `2.2259` n `113`; fx avg `0.0134` n `6`; index avg `0.2111` n `25`; metal avg `0.2517` n `20`; unknown avg `-0.0902` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2291`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2279`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2141`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2054`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
