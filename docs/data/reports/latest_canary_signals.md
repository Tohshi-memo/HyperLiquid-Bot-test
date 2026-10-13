# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T06:37:26.442622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `13`; crypto_alt avg `0.1752` n `235`; crypto_major avg `0.1391` n `8`; equity avg `-0.0207` n `151`; fx avg `-0.0127` n `6`; index avg `-0.0162` n `26`; metal avg `-0.0287` n `20`; unknown avg `0.0861` n `1135`
- 1h: commodity avg `-0.0034` n `13`; crypto_alt avg `0.3344` n `235`; crypto_major avg `0.3558` n `8`; equity avg `-0.1987` n `151`; fx avg `0.0098` n `6`; index avg `-0.0185` n `26`; metal avg `-0.0786` n `20`; unknown avg `0.7935` n `1117`
- 4h: commodity avg `-0.0618` n `13`; crypto_alt avg `2.2616` n `235`; crypto_major avg `1.297` n `8`; equity avg `0.397` n `151`; fx avg `0.0832` n `6`; index avg `0.0689` n `26`; metal avg `0.0857` n `20`; unknown avg `1.3134` n `1075`
- 24h: commodity avg `0.3332` n `13`; crypto_alt avg `-3.5498` n `235`; crypto_major avg `-2.0643` n `8`; equity avg `-3.5196` n `151`; fx avg `0.0307` n `6`; index avg `-0.4759` n `26`; metal avg `-0.0829` n `20`; unknown avg `0.5538` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1965`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1802`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1466`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1239`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0829`, n `666`, weak_sample_signal
