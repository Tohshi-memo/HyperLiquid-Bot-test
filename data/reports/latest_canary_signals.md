# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T01:22:30.879212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.024` n `12`; crypto_alt avg `0.0091` n `230`; crypto_major avg `0.0157` n `8`; equity avg `-0.0044` n `114`; fx avg `0.0036` n `6`; index avg `0.0016` n `25`; metal avg `0.0015` n `20`; unknown avg `0.1116` n `791`
- 1h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.0897` n `230`; crypto_major avg `0.0606` n `8`; equity avg `-0.0331` n `114`; fx avg `-0.0008` n `6`; index avg `0.0016` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.038` n `791`
- 4h: commodity avg `0.0216` n `12`; crypto_alt avg `-0.5101` n `230`; crypto_major avg `-0.2313` n `8`; equity avg `-0.0172` n `114`; fx avg `-0.0001` n `6`; index avg `0.0168` n `25`; metal avg `0.0082` n `20`; unknown avg `0.1023` n `791`
- 24h: commodity avg `-0.0066` n `12`; crypto_alt avg `0.1565` n `230`; crypto_major avg `0.0783` n `8`; equity avg `0.1565` n `114`; fx avg `0.0454` n `6`; index avg `0.0168` n `25`; metal avg `-0.0294` n `20`; unknown avg `0.1166` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2241`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
