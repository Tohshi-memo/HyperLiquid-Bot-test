# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T22:52:26.188046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.0777` n `230`; crypto_major avg `-0.0225` n `8`; equity avg `0.0652` n `113`; fx avg `0.0041` n `6`; index avg `0.0022` n `25`; metal avg `0.0133` n `20`; unknown avg `-0.0992` n `786`
- 1h: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.0988` n `230`; crypto_major avg `-0.1238` n `8`; equity avg `-0.0438` n `113`; fx avg `0.0023` n `6`; index avg `-0.0177` n `25`; metal avg `-0.05` n `20`; unknown avg `-0.1373` n `786`
- 4h: commodity avg `-0.1006` n `12`; crypto_alt avg `-1.0177` n `230`; crypto_major avg `-0.5452` n `8`; equity avg `-0.3119` n `113`; fx avg `-0.0054` n `6`; index avg `-0.0198` n `25`; metal avg `-0.1365` n `20`; unknown avg `-0.3906` n `786`
- 24h: commodity avg `-0.028` n `12`; crypto_alt avg `-1.6889` n `230`; crypto_major avg `-0.6038` n `8`; equity avg `2.7873` n `113`; fx avg `0.0226` n `6`; index avg `0.3886` n `25`; metal avg `0.0914` n `20`; unknown avg `-0.1382` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2338`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
