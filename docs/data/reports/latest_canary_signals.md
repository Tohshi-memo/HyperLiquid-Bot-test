# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T07:07:27.991506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0922` n `12`; crypto_alt avg `0.0123` n `230`; crypto_major avg `0.1903` n `8`; equity avg `0.1189` n `113`; fx avg `0.0163` n `6`; index avg `0.0036` n `25`; metal avg `-0.0448` n `20`; unknown avg `0.041` n `786`
- 1h: commodity avg `-0.0382` n `12`; crypto_alt avg `-0.215` n `230`; crypto_major avg `0.0676` n `8`; equity avg `0.0935` n `113`; fx avg `0.0335` n `6`; index avg `0.0127` n `25`; metal avg `0.1224` n `20`; unknown avg `0.0048` n `786`
- 4h: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.6287` n `230`; crypto_major avg `-0.0139` n `8`; equity avg `0.0828` n `113`; fx avg `0.005` n `6`; index avg `0.0007` n `25`; metal avg `-0.0297` n `20`; unknown avg `-0.0131` n `770`
- 24h: commodity avg `0.0216` n `12`; crypto_alt avg `-1.0322` n `230`; crypto_major avg `0.8613` n `8`; equity avg `2.1535` n `113`; fx avg `0.0184` n `6`; index avg `0.2176` n `25`; metal avg `0.2585` n `20`; unknown avg `-0.0512` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2261`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2192`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2077`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
