# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T17:22:28.786347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0599` n `12`; crypto_alt avg `0.1965` n `230`; crypto_major avg `0.1892` n `8`; equity avg `-0.2134` n `114`; fx avg `0.0052` n `6`; index avg `-0.0267` n `25`; metal avg `-0.028` n `20`; unknown avg `0.0757` n `792`
- 1h: commodity avg `0.2245` n `12`; crypto_alt avg `0.1282` n `230`; crypto_major avg `0.0815` n `8`; equity avg `-0.1957` n `114`; fx avg `0.0128` n `6`; index avg `-0.0688` n `25`; metal avg `-0.071` n `20`; unknown avg `0.1803` n `792`
- 4h: commodity avg `0.2037` n `12`; crypto_alt avg `0.3301` n `230`; crypto_major avg `0.6956` n `8`; equity avg `0.651` n `114`; fx avg `0.0124` n `6`; index avg `0.0363` n `25`; metal avg `0.2103` n `20`; unknown avg `0.2901` n `792`
- 24h: commodity avg `0.2049` n `12`; crypto_alt avg `0.0436` n `230`; crypto_major avg `0.8733` n `8`; equity avg `1.4444` n `114`; fx avg `0.0206` n `6`; index avg `0.1482` n `25`; metal avg `0.2401` n `20`; unknown avg `0.2365` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
