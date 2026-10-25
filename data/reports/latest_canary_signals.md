# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T15:52:25.820487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0332` n `13`; crypto_alt avg `0.0968` n `237`; crypto_major avg `-0.0711` n `8`; equity avg `0.0202` n `152`; fx avg `0.0055` n `6`; index avg `0.0` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.3278` n `1240`
- 1h: commodity avg `-0.0128` n `13`; crypto_alt avg `0.5915` n `237`; crypto_major avg `0.2186` n `8`; equity avg `0.081` n `152`; fx avg `-0.0062` n `6`; index avg `0.0048` n `26`; metal avg `-0.0059` n `20`; unknown avg `-0.219` n `1232`
- 4h: commodity avg `-0.0786` n `13`; crypto_alt avg `0.6059` n `237`; crypto_major avg `0.1908` n `8`; equity avg `0.3241` n `152`; fx avg `0.0059` n `6`; index avg `0.0441` n `26`; metal avg `0.0387` n `20`; unknown avg `-0.1399` n `1225`
- 24h: commodity avg `-0.1829` n `13`; crypto_alt avg `1.6174` n `237`; crypto_major avg `2.0302` n `8`; equity avg `0.9594` n `152`; fx avg `0.03` n `6`; index avg `0.1642` n `26`; metal avg `0.1535` n `20`; unknown avg `18.9031` n `1081`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
