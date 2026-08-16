# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T09:22:31.548327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.014` n `230`; crypto_major avg `0.0028` n `8`; equity avg `-0.0311` n `114`; fx avg `0.0025` n `6`; index avg `0.0017` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0783` n `791`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `0.0353` n `230`; crypto_major avg `0.0326` n `8`; equity avg `-0.0078` n `114`; fx avg `0.0021` n `6`; index avg `0.0027` n `25`; metal avg `0.0059` n `20`; unknown avg `0.0765` n `791`
- 4h: commodity avg `0.0188` n `12`; crypto_alt avg `0.4287` n `230`; crypto_major avg `0.1914` n `8`; equity avg `0.1048` n `114`; fx avg `-0.0006` n `6`; index avg `0.0203` n `25`; metal avg `0.0166` n `20`; unknown avg `0.003` n `759`
- 24h: commodity avg `0.1` n `12`; crypto_alt avg `0.013` n `230`; crypto_major avg `0.2908` n `8`; equity avg `0.4034` n `114`; fx avg `-0.0102` n `6`; index avg `0.0484` n `25`; metal avg `0.0188` n `20`; unknown avg `0.0701` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
