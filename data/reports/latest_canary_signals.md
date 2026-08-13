# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T05:07:33.501620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0302` n `12`; crypto_alt avg `0.0924` n `230`; crypto_major avg `0.1947` n `8`; equity avg `0.0675` n `113`; fx avg `-0.0024` n `6`; index avg `-0.0028` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.2534` n `787`
- 1h: commodity avg `0.062` n `12`; crypto_alt avg `0.0788` n `230`; crypto_major avg `0.2631` n `8`; equity avg `0.0167` n `113`; fx avg `-0.0197` n `6`; index avg `-0.0236` n `25`; metal avg `0.015` n `20`; unknown avg `1.2098` n `787`
- 4h: commodity avg `0.176` n `12`; crypto_alt avg `0.3602` n `230`; crypto_major avg `0.6425` n `8`; equity avg `0.2934` n `113`; fx avg `0.0117` n `6`; index avg `0.029` n `25`; metal avg `-0.2477` n `20`; unknown avg `1.1427` n `786`
- 24h: commodity avg `-0.1009` n `12`; crypto_alt avg `-0.9551` n `230`; crypto_major avg `0.2742` n `8`; equity avg `2.5766` n `113`; fx avg `-0.0543` n `6`; index avg `0.3296` n `25`; metal avg `-0.1517` n `20`; unknown avg `0.1603` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2426`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
