# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T13:22:33.295977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.116` n `13`; crypto_alt avg `0.0088` n `235`; crypto_major avg `0.0219` n `8`; equity avg `-0.0975` n `150`; fx avg `-0.0224` n `6`; index avg `-0.0204` n `26`; metal avg `-0.0117` n `20`; unknown avg `2.1416` n `1074`
- 1h: commodity avg `0.3012` n `13`; crypto_alt avg `-0.0132` n `235`; crypto_major avg `-0.1182` n `8`; equity avg `-0.0711` n `150`; fx avg `-0.0428` n `6`; index avg `-0.0272` n `26`; metal avg `-0.0999` n `20`; unknown avg `4.9241` n `1070`
- 4h: commodity avg `0.0027` n `13`; crypto_alt avg `0.3645` n `235`; crypto_major avg `-0.0031` n `8`; equity avg `0.2885` n `150`; fx avg `0.0526` n `6`; index avg `0.0794` n `26`; metal avg `-0.0143` n `20`; unknown avg `2.5465` n `1064`
- 24h: commodity avg `-0.3682` n `13`; crypto_alt avg `-0.3508` n `235`; crypto_major avg `-0.1476` n `8`; equity avg `0.7315` n `149`; fx avg `0.0688` n `6`; index avg `0.2556` n `26`; metal avg `-0.1256` n `20`; unknown avg `2.4166` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
