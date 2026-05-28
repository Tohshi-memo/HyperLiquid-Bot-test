# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T18:37:25.466707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3983` n `12`; crypto_alt avg `-0.3335` n `228`; crypto_major avg `-0.223` n `8`; equity avg `-0.1653` n `69`; fx avg `0.0031` n `6`; index avg `-0.0934` n `23`; metal avg `-0.1315` n `18`; unknown avg `-0.0239` n `417`
- 1h: commodity avg `0.4035` n `12`; crypto_alt avg `0.3992` n `228`; crypto_major avg `0.2787` n `8`; equity avg `0.406` n `69`; fx avg `0.0132` n `6`; index avg `-0.048` n `23`; metal avg `-0.0401` n `18`; unknown avg `0.1239` n `417`
- 4h: commodity avg `0.3984` n `12`; crypto_alt avg `2.0393` n `228`; crypto_major avg `1.9844` n `8`; equity avg `1.5083` n `69`; fx avg `-0.0066` n `6`; index avg `0.8721` n `23`; metal avg `1.0445` n `18`; unknown avg `0.4619` n `417`
- 24h: commodity avg `1.3021` n `12`; crypto_alt avg `-2.7379` n `228`; crypto_major avg `-0.5797` n `8`; equity avg `1.3994` n `68`; fx avg `-0.0042` n `6`; index avg `0.9171` n `23`; metal avg `0.6138` n `18`; unknown avg `-0.7446` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
