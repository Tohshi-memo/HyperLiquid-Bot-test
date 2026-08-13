# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T13:37:27.874603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.0749` n `230`; crypto_major avg `0.1179` n `8`; equity avg `0.8577` n `113`; fx avg `-0.0082` n `6`; index avg `0.0655` n `25`; metal avg `-0.1031` n `20`; unknown avg `0.0247` n `787`
- 1h: commodity avg `-0.1886` n `12`; crypto_alt avg `0.0313` n `230`; crypto_major avg `0.2002` n `8`; equity avg `0.9828` n `113`; fx avg `-0.0009` n `6`; index avg `0.1082` n `25`; metal avg `-0.1068` n `20`; unknown avg `0.103` n `787`
- 4h: commodity avg `-0.1835` n `12`; crypto_alt avg `0.1068` n `230`; crypto_major avg `0.1779` n `8`; equity avg `1.1211` n `113`; fx avg `-0.0133` n `6`; index avg `0.1428` n `25`; metal avg `-0.0297` n `20`; unknown avg `0.141` n `787`
- 24h: commodity avg `-0.4459` n `12`; crypto_alt avg `-0.6513` n `230`; crypto_major avg `0.0835` n `8`; equity avg `1.6439` n `113`; fx avg `0.0195` n `6`; index avg `0.1699` n `25`; metal avg `-0.5237` n `20`; unknown avg `0.3748` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2301`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1989`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1945`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
