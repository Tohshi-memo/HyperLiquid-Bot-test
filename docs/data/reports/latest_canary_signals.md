# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T13:52:23.567456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.41` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0729` n `12`; crypto_alt avg `-0.186` n `228`; crypto_major avg `-0.1617` n `8`; equity avg `0.213` n `69`; fx avg `-0.0302` n `6`; index avg `0.1989` n `23`; metal avg `-0.0206` n `18`; unknown avg `-0.1211` n `422`
- 1h: commodity avg `0.4274` n `12`; crypto_alt avg `0.0424` n `228`; crypto_major avg `-0.192` n `8`; equity avg `-0.2755` n `69`; fx avg `-0.0238` n `6`; index avg `0.0983` n `23`; metal avg `-0.3542` n `18`; unknown avg `-0.1133` n `422`
- 4h: commodity avg `0.1374` n `12`; crypto_alt avg `0.9042` n `228`; crypto_major avg `0.3155` n `8`; equity avg `-0.2755` n `69`; fx avg `-0.0149` n `6`; index avg `0.1639` n `23`; metal avg `-0.4066` n `18`; unknown avg `0.9307` n `422`
- 24h: commodity avg `-1.0044` n `12`; crypto_alt avg `1.1079` n `228`; crypto_major avg `-0.8792` n `8`; equity avg `0.9478` n `69`; fx avg `0.2055` n `6`; index avg `0.4526` n `23`; metal avg `1.444` n `18`; unknown avg `0.1394` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
