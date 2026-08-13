# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T04:07:24.887568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0405` n `12`; crypto_alt avg `-0.0496` n `230`; crypto_major avg `-0.0012` n `8`; equity avg `0.0361` n `113`; fx avg `0.002` n `6`; index avg `0.0193` n `25`; metal avg `-0.0674` n `20`; unknown avg `-0.0999` n `787`
- 1h: commodity avg `0.1114` n `12`; crypto_alt avg `0.1614` n `230`; crypto_major avg `0.13` n `8`; equity avg `0.0509` n `113`; fx avg `0.0073` n `6`; index avg `0.0299` n `25`; metal avg `-0.0739` n `20`; unknown avg `0.0687` n `786`
- 4h: commodity avg `0.0137` n `12`; crypto_alt avg `0.3025` n `230`; crypto_major avg `0.3995` n `8`; equity avg `0.1759` n `113`; fx avg `0.0152` n `6`; index avg `0.0346` n `25`; metal avg `-0.1852` n `20`; unknown avg `-0.0561` n `786`
- 24h: commodity avg `-0.2288` n `12`; crypto_alt avg `-1.1934` n `230`; crypto_major avg `-0.1062` n `8`; equity avg `2.4573` n `113`; fx avg `-0.0373` n `6`; index avg `0.3196` n `25`; metal avg `-0.1434` n `20`; unknown avg `-0.007` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2411`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2077`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1905`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
