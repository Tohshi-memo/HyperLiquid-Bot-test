# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T17:07:33.492652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0361` n `12`; crypto_alt avg `0.0066` n `230`; crypto_major avg `0.023` n `8`; equity avg `-0.1162` n `113`; fx avg `-0.0041` n `6`; index avg `-0.0303` n `25`; metal avg `0.0247` n `20`; unknown avg `-0.0376` n `785`
- 1h: commodity avg `0.0641` n `12`; crypto_alt avg `0.1716` n `230`; crypto_major avg `0.0786` n `8`; equity avg `-0.1284` n `113`; fx avg `-0.009` n `6`; index avg `-0.0518` n `25`; metal avg `0.0122` n `20`; unknown avg `-0.0295` n `785`
- 4h: commodity avg `0.1917` n `12`; crypto_alt avg `-1.238` n `230`; crypto_major avg `-0.7928` n `8`; equity avg `-0.1419` n `113`; fx avg `-0.0055` n `6`; index avg `-0.1172` n `25`; metal avg `-0.1092` n `20`; unknown avg `0.0938` n `785`
- 24h: commodity avg `0.1755` n `12`; crypto_alt avg `-1.8353` n `230`; crypto_major avg `-0.1399` n `8`; equity avg `-0.0222` n `113`; fx avg `-0.0573` n `6`; index avg `0.0463` n `25`; metal avg `0.0663` n `20`; unknown avg `-0.2908` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1931`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
