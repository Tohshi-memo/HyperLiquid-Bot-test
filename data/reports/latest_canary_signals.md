# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T08:07:32.494364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.0739` n `230`; crypto_major avg `-0.1384` n `8`; equity avg `-0.0081` n `114`; fx avg `-0.0223` n `6`; index avg `-0.01` n `25`; metal avg `-0.074` n `20`; unknown avg `0.0178` n `792`
- 1h: commodity avg `0.0495` n `12`; crypto_alt avg `-0.1625` n `230`; crypto_major avg `-0.2109` n `8`; equity avg `0.0707` n `114`; fx avg `-0.0027` n `6`; index avg `0.0001` n `25`; metal avg `-0.0301` n `20`; unknown avg `0.0239` n `792`
- 4h: commodity avg `-0.0228` n `12`; crypto_alt avg `-0.0711` n `230`; crypto_major avg `-0.0022` n `8`; equity avg `0.5475` n `114`; fx avg `-0.0163` n `6`; index avg `0.0772` n `25`; metal avg `0.0057` n `20`; unknown avg `0.0278` n `776`
- 24h: commodity avg `-0.1963` n `12`; crypto_alt avg `0.088` n `230`; crypto_major avg `0.6944` n `8`; equity avg `1.2255` n `114`; fx avg `-0.0426` n `6`; index avg `0.1468` n `25`; metal avg `0.2081` n `20`; unknown avg `0.1175` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
