# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T23:22:28.809494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.1037` n `230`; crypto_major avg `0.1372` n `8`; equity avg `-0.0088` n `114`; fx avg `0.0034` n `6`; index avg `-0.0062` n `25`; metal avg `0.0185` n `20`; unknown avg `-0.064` n `793`
- 1h: commodity avg `-0.0356` n `12`; crypto_alt avg `-0.0872` n `230`; crypto_major avg `0.1131` n `8`; equity avg `-0.1096` n `114`; fx avg `-0.0388` n `6`; index avg `-0.0102` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.1295` n `793`
- 4h: commodity avg `0.0943` n `12`; crypto_alt avg `-0.2629` n `230`; crypto_major avg `0.1592` n `8`; equity avg `0.0748` n `114`; fx avg `-0.0194` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0171` n `20`; unknown avg `-0.124` n `792`
- 24h: commodity avg `0.543` n `12`; crypto_alt avg `0.4107` n `230`; crypto_major avg `1.518` n `8`; equity avg `1.0992` n `114`; fx avg `-0.0015` n `6`; index avg `0.0485` n `25`; metal avg `0.1758` n `20`; unknown avg `0.2879` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
