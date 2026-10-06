# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T23:37:35.833538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0208` n `13`; crypto_alt avg `-0.1162` n `235`; crypto_major avg `-0.0316` n `8`; equity avg `-0.0216` n `150`; fx avg `0.0141` n `6`; index avg `-0.0081` n `26`; metal avg `0.0142` n `20`; unknown avg `0.6728` n `1076`
- 1h: commodity avg `0.0488` n `13`; crypto_alt avg `0.0462` n `235`; crypto_major avg `-0.0584` n `8`; equity avg `-0.027` n `150`; fx avg `0.0156` n `6`; index avg `-0.0016` n `26`; metal avg `0.0328` n `20`; unknown avg `0.5469` n `1074`
- 4h: commodity avg `0.1163` n `13`; crypto_alt avg `0.1299` n `235`; crypto_major avg `0.051` n `8`; equity avg `0.191` n `150`; fx avg `0.0089` n `6`; index avg `0.0241` n `26`; metal avg `0.003` n `20`; unknown avg `0.8097` n `990`
- 24h: commodity avg `0.3862` n `13`; crypto_alt avg `-1.2521` n `235`; crypto_major avg `-0.9172` n `8`; equity avg `0.3291` n `149`; fx avg `0.1022` n `6`; index avg `-0.017` n `26`; metal avg `0.0797` n `20`; unknown avg `871.1722` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
