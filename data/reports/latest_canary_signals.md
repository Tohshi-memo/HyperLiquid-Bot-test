# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T18:52:30.995066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.1746` n `234`; crypto_major avg `-0.1506` n `8`; equity avg `0.01` n `140`; fx avg `-0.0022` n `6`; index avg `0.0007` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.931` n `943`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `-0.2195` n `234`; crypto_major avg `-0.1584` n `8`; equity avg `0.0445` n `140`; fx avg `-0.0002` n `6`; index avg `0.0127` n `26`; metal avg `0.005` n `20`; unknown avg `0.0591` n `941`
- 4h: commodity avg `-0.0245` n `12`; crypto_alt avg `-0.1352` n `234`; crypto_major avg `-0.2897` n `8`; equity avg `0.0507` n `140`; fx avg `-0.0201` n `6`; index avg `0.0254` n `26`; metal avg `-0.0114` n `20`; unknown avg `5.4711` n `882`
- 24h: commodity avg `0.0409` n `12`; crypto_alt avg `2.1302` n `234`; crypto_major avg `0.8547` n `8`; equity avg `0.4255` n `140`; fx avg `0.0051` n `6`; index avg `0.0932` n `26`; metal avg `-0.0521` n `20`; unknown avg `2.2355` n `792`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
