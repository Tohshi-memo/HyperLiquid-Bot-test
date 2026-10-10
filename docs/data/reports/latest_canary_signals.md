# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T05:37:28.060068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `13`; crypto_alt avg `0.065` n `235`; crypto_major avg `0.1545` n `8`; equity avg `-0.003` n `150`; fx avg `0.0007` n `6`; index avg `0.001` n `26`; metal avg `-0.0044` n `20`; unknown avg `0.2593` n `1116`
- 1h: commodity avg `0.0175` n `13`; crypto_alt avg `0.3581` n `235`; crypto_major avg `0.3109` n `8`; equity avg `0.0104` n `150`; fx avg `-0.0008` n `6`; index avg `0.0062` n `26`; metal avg `-0.0164` n `20`; unknown avg `0.1424` n `1114`
- 4h: commodity avg `0.0085` n `13`; crypto_alt avg `0.8173` n `235`; crypto_major avg `0.4265` n `8`; equity avg `0.046` n `150`; fx avg `0.0054` n `6`; index avg `0.0137` n `26`; metal avg `-0.0156` n `20`; unknown avg `0.0963` n `1108`
- 24h: commodity avg `0.0808` n `13`; crypto_alt avg `1.8518` n `235`; crypto_major avg `0.0964` n `8`; equity avg `0.0471` n `150`; fx avg `-0.0424` n `6`; index avg `0.0355` n `26`; metal avg `-0.0237` n `20`; unknown avg `12.6282` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
