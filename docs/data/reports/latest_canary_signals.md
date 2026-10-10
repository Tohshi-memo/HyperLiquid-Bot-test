# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T19:22:27.371448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `0.1485` n `235`; crypto_major avg `0.0952` n `8`; equity avg `0.0131` n `150`; fx avg `0.0012` n `6`; index avg `0.0015` n `26`; metal avg `-0.0077` n `20`; unknown avg `3.7443` n `1117`
- 1h: commodity avg `0.0191` n `13`; crypto_alt avg `0.1003` n `235`; crypto_major avg `0.0757` n `8`; equity avg `0.0244` n `150`; fx avg `0.0017` n `6`; index avg `-0.0013` n `26`; metal avg `0.0033` n `20`; unknown avg `0.3292` n `1043`
- 4h: commodity avg `0.0015` n `13`; crypto_alt avg `0.4108` n `235`; crypto_major avg `-0.1298` n `8`; equity avg `-0.0144` n `150`; fx avg `-0.0039` n `6`; index avg `-0.0211` n `26`; metal avg `-0.0223` n `20`; unknown avg `0.7476` n `1023`
- 24h: commodity avg `-0.1354` n `13`; crypto_alt avg `2.967` n `235`; crypto_major avg `1.0402` n `8`; equity avg `0.0859` n `150`; fx avg `-0.0067` n `6`; index avg `-0.0055` n `26`; metal avg `-0.0235` n `20`; unknown avg `0.9278` n `944`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
