# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T01:41:07.775506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.1817` n `230`; crypto_major avg `0.1881` n `8`; equity avg `0.229` n `108`; fx avg `-0.0215` n `6`; index avg `0.029` n `25`; metal avg `0.0431` n `20`; unknown avg `0.285` n `781`
- 1h: commodity avg `0.1393` n `12`; crypto_alt avg `0.2506` n `230`; crypto_major avg `0.1434` n `8`; equity avg `-0.2913` n `108`; fx avg `-0.0379` n `6`; index avg `-0.0668` n `25`; metal avg `-0.0325` n `20`; unknown avg `0.4154` n `781`
- 4h: commodity avg `0.1988` n `12`; crypto_alt avg `0.1417` n `230`; crypto_major avg `-0.0059` n `8`; equity avg `0.4174` n `108`; fx avg `-0.0818` n `6`; index avg `0.0417` n `25`; metal avg `0.0111` n `20`; unknown avg `-0.0501` n `781`
- 24h: commodity avg `-1.1825` n `12`; crypto_alt avg `0.3084` n `230`; crypto_major avg `0.6344` n `8`; equity avg `3.8076` n `107`; fx avg `0.0731` n `6`; index avg `0.8357` n `25`; metal avg `0.7937` n `20`; unknown avg `0.3473` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
