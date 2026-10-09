# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T21:37:29.309681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `13`; crypto_alt avg `-0.0026` n `235`; crypto_major avg `-0.0222` n `8`; equity avg `-0.0096` n `150`; fx avg `-0.0022` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0059` n `20`; unknown avg `-0.0728` n `1108`
- 1h: commodity avg `-0.0379` n `13`; crypto_alt avg `0.5588` n `235`; crypto_major avg `0.3529` n `8`; equity avg `0.0111` n `150`; fx avg `0.0019` n `6`; index avg `0.0141` n `26`; metal avg `-0.0141` n `20`; unknown avg `2.801` n `1098`
- 4h: commodity avg `-0.2868` n `13`; crypto_alt avg `0.2133` n `235`; crypto_major avg `-0.106` n `8`; equity avg `0.0751` n `150`; fx avg `0.0139` n `6`; index avg `0.0317` n `26`; metal avg `0.0217` n `20`; unknown avg `2.5984` n `1026`
- 24h: commodity avg `-0.2123` n `13`; crypto_alt avg `1.7737` n `235`; crypto_major avg `0.3258` n `8`; equity avg `0.8589` n `150`; fx avg `0.0123` n `6`; index avg `0.1539` n `26`; metal avg `0.5975` n `20`; unknown avg `12.892` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
