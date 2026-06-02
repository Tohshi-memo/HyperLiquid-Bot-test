# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T01:07:21.458748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.51` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.149` n `12`; crypto_alt avg `-0.1556` n `228`; crypto_major avg `-0.1617` n `8`; equity avg `-0.0234` n `69`; fx avg `-0.0332` n `6`; index avg `0.001` n `23`; metal avg `0.1543` n `18`; unknown avg `-0.2302` n `422`
- 1h: commodity avg `-0.1009` n `12`; crypto_alt avg `-0.4656` n `228`; crypto_major avg `-0.2097` n `8`; equity avg `-0.4238` n `69`; fx avg `-0.0444` n `6`; index avg `-0.3113` n `23`; metal avg `0.1799` n `18`; unknown avg `-0.523` n `422`
- 4h: commodity avg `-0.2577` n `12`; crypto_alt avg `-0.2619` n `228`; crypto_major avg `0.1018` n `8`; equity avg `-0.8416` n `69`; fx avg `-0.0223` n `6`; index avg `-0.4721` n `23`; metal avg `0.1977` n `18`; unknown avg `-0.269` n `422`
- 24h: commodity avg `-0.3679` n `12`; crypto_alt avg `-0.9179` n `228`; crypto_major avg `-1.3937` n `8`; equity avg `-1.4166` n `69`; fx avg `-0.0281` n `6`; index avg `-0.4135` n `23`; metal avg `-0.0453` n `18`; unknown avg `1.4215` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
