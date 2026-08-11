# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T10:07:31.313863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `-0.0549` n `230`; crypto_major avg `0.0251` n `8`; equity avg `-0.054` n `113`; fx avg `-0.0036` n `6`; index avg `-0.0088` n `25`; metal avg `-0.0047` n `20`; unknown avg `-0.0458` n `785`
- 1h: commodity avg `-0.0869` n `12`; crypto_alt avg `0.1026` n `230`; crypto_major avg `0.2038` n `8`; equity avg `0.24` n `113`; fx avg `-0.0076` n `6`; index avg `0.0375` n `25`; metal avg `0.0671` n `20`; unknown avg `-0.005` n `785`
- 4h: commodity avg `0.2788` n `12`; crypto_alt avg `-0.1494` n `230`; crypto_major avg `0.2944` n `8`; equity avg `-0.2363` n `113`; fx avg `-0.0009` n `6`; index avg `-0.0227` n `25`; metal avg `0.0712` n `20`; unknown avg `0.0388` n `785`
- 24h: commodity avg `1.0763` n `12`; crypto_alt avg `-1.046` n `230`; crypto_major avg `-0.4384` n `8`; equity avg `-1.3928` n `113`; fx avg `0.006` n `6`; index avg `-0.0297` n `25`; metal avg `0.3632` n `20`; unknown avg `0.1616` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1694`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
