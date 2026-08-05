# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T02:37:34.073994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1344` n `12`; crypto_alt avg `0.1461` n `230`; crypto_major avg `0.1508` n `8`; equity avg `-0.0419` n `108`; fx avg `0.0033` n `6`; index avg `-0.0196` n `25`; metal avg `0.1894` n `20`; unknown avg `-0.0925` n `781`
- 1h: commodity avg `-0.3372` n `12`; crypto_alt avg `0.2141` n `230`; crypto_major avg `0.4255` n `8`; equity avg `0.1966` n `108`; fx avg `-0.0153` n `6`; index avg `0.0029` n `25`; metal avg `0.3184` n `20`; unknown avg `-0.1901` n `781`
- 4h: commodity avg `-0.1261` n `12`; crypto_alt avg `0.3615` n `230`; crypto_major avg `0.4364` n `8`; equity avg `0.4816` n `108`; fx avg `-0.0879` n `6`; index avg `0.0422` n `25`; metal avg `0.2815` n `20`; unknown avg `-0.1771` n `781`
- 24h: commodity avg `-1.5809` n `12`; crypto_alt avg `0.178` n `230`; crypto_major avg `0.6927` n `8`; equity avg `3.7865` n `107`; fx avg `0.0194` n `6`; index avg `0.7617` n `25`; metal avg `1.0631` n `20`; unknown avg `0.3995` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
