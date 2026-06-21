# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T14:37:29.385497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `0.133` n `228`; crypto_major avg `0.1598` n `8`; equity avg `-0.0245` n `78`; fx avg `-0.0021` n `6`; index avg `0.0023` n `23`; metal avg `-0.0081` n `18`; unknown avg `0.0193` n `702`
- 1h: commodity avg `0.0462` n `12`; crypto_alt avg `0.1142` n `228`; crypto_major avg `0.2416` n `8`; equity avg `-0.0431` n `78`; fx avg `0.0189` n `6`; index avg `-0.0051` n `23`; metal avg `-0.0284` n `18`; unknown avg `-0.033` n `702`
- 4h: commodity avg `0.1257` n `12`; crypto_alt avg `-0.077` n `228`; crypto_major avg `-0.3354` n `8`; equity avg `-0.1081` n `78`; fx avg `0.0428` n `6`; index avg `-0.0046` n `23`; metal avg `-0.0796` n `18`; unknown avg `0.1485` n `702`
- 24h: commodity avg `-0.0681` n `12`; crypto_alt avg `2.3849` n `228`; crypto_major avg `0.7172` n `8`; equity avg `0.5295` n `78`; fx avg `0.0485` n `6`; index avg `0.0521` n `23`; metal avg `-0.0358` n `18`; unknown avg `1.3335` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
