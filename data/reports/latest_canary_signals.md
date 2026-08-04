# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T16:52:29.510445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.9899` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.058` n `12`; crypto_alt avg `-0.0082` n `230`; crypto_major avg `-0.0251` n `8`; equity avg `0.029` n `107`; fx avg `-0.0002` n `6`; index avg `0.0135` n `25`; metal avg `0.0124` n `20`; unknown avg `0.0353` n `782`
- 1h: commodity avg `0.1523` n `12`; crypto_alt avg `-0.166` n `230`; crypto_major avg `-0.3097` n `8`; equity avg `0.0788` n `107`; fx avg `0.0212` n `6`; index avg `0.0304` n `25`; metal avg `0.0707` n `20`; unknown avg `0.0602` n `782`
- 4h: commodity avg `-0.3726` n `12`; crypto_alt avg `-0.1617` n `230`; crypto_major avg `-0.2456` n `8`; equity avg `1.7443` n `107`; fx avg `0.031` n `6`; index avg `0.4137` n `25`; metal avg `0.1808` n `20`; unknown avg `-0.1753` n `781`
- 24h: commodity avg `-0.9973` n `12`; crypto_alt avg `-0.2641` n `230`; crypto_major avg `0.1453` n `8`; equity avg `4.3517` n `107`; fx avg `0.0921` n `6`; index avg `0.8092` n `25`; metal avg `1.1687` n `20`; unknown avg `0.4341` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
