# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T19:37:30.040921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `0.0589` n `230`; crypto_major avg `0.0174` n `8`; equity avg `0.1192` n `114`; fx avg `-0.0014` n `6`; index avg `0.0084` n `25`; metal avg `0.0362` n `20`; unknown avg `-0.0938` n `791`
- 1h: commodity avg `-0.078` n `12`; crypto_alt avg `-0.1498` n `230`; crypto_major avg `-0.0874` n `8`; equity avg `0.0728` n `114`; fx avg `0.0061` n `6`; index avg `0.0148` n `25`; metal avg `0.0238` n `20`; unknown avg `8.5613` n `791`
- 4h: commodity avg `-0.0233` n `12`; crypto_alt avg `0.3139` n `230`; crypto_major avg `-0.3421` n `8`; equity avg `0.074` n `114`; fx avg `0.0087` n `6`; index avg `0.0217` n `25`; metal avg `0.0089` n `20`; unknown avg `18.4062` n `791`
- 24h: commodity avg `0.1824` n `12`; crypto_alt avg `0.2165` n `230`; crypto_major avg `-1.0826` n `8`; equity avg `-0.5365` n `114`; fx avg `0.0743` n `6`; index avg `-0.0827` n `25`; metal avg `0.2493` n `20`; unknown avg `-0.0822` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
