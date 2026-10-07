# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T01:37:31.964125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `13`; crypto_alt avg `-0.3941` n `235`; crypto_major avg `-0.2091` n `8`; equity avg `-0.1231` n `150`; fx avg `0.0098` n `6`; index avg `-0.0045` n `26`; metal avg `0.0386` n `20`; unknown avg `0.0564` n `1076`
- 1h: commodity avg `0.1098` n `13`; crypto_alt avg `-0.5671` n `235`; crypto_major avg `-0.4361` n `8`; equity avg `-0.3929` n `150`; fx avg `-0.02` n `6`; index avg `-0.057` n `26`; metal avg `-0.0211` n `20`; unknown avg `0.2639` n `1074`
- 4h: commodity avg `0.2421` n `13`; crypto_alt avg `-0.7881` n `235`; crypto_major avg `-0.5064` n `8`; equity avg `-0.1775` n `150`; fx avg `-0.0045` n `6`; index avg `-0.0131` n `26`; metal avg `-0.0511` n `20`; unknown avg `0.3599` n `1052`
- 24h: commodity avg `0.4946` n `13`; crypto_alt avg `-1.2985` n `235`; crypto_major avg `-1.1929` n `8`; equity avg `0.2937` n `149`; fx avg `0.055` n `6`; index avg `0.0161` n `26`; metal avg `0.021` n `20`; unknown avg `870.8631` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
