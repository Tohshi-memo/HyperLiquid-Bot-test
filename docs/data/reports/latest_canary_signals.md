# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T01:07:20.359178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `0.0783` n `228`; crypto_major avg `0.0279` n `8`; equity avg `-0.13` n `69`; fx avg `0.017` n `6`; index avg `-0.0702` n `23`; metal avg `0.1628` n `18`; unknown avg `-0.0304` n `417`
- 1h: commodity avg `-0.0307` n `12`; crypto_alt avg `0.5394` n `228`; crypto_major avg `0.33` n `8`; equity avg `-0.0763` n `69`; fx avg `0.045` n `6`; index avg `-0.0894` n `23`; metal avg `0.1141` n `18`; unknown avg `0.0013` n `417`
- 4h: commodity avg `-0.352` n `12`; crypto_alt avg `0.4321` n `228`; crypto_major avg `0.3076` n `8`; equity avg `0.3409` n `69`; fx avg `0.0828` n `6`; index avg `-0.0913` n `23`; metal avg `0.1762` n `18`; unknown avg `-0.1798` n `417`
- 24h: commodity avg `0.4598` n `12`; crypto_alt avg `-1.2683` n `228`; crypto_major avg `0.5224` n `8`; equity avg `2.4014` n `69`; fx avg `0.0767` n `6`; index avg `0.735` n `23`; metal avg `0.8882` n `18`; unknown avg `0.0152` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
