# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T08:52:31.108493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0274` n `12`; crypto_alt avg `0.1316` n `228`; crypto_major avg `0.0364` n `8`; equity avg `0.0074` n `78`; fx avg `-0.0041` n `6`; index avg `0.006` n `23`; metal avg `-0.0058` n `18`; unknown avg `0.0241` n `702`
- 1h: commodity avg `0.0268` n `12`; crypto_alt avg `-0.1354` n `228`; crypto_major avg `-0.4993` n `8`; equity avg `-0.091` n `78`; fx avg `-0.0102` n `6`; index avg `-0.002` n `23`; metal avg `-0.0168` n `18`; unknown avg `-0.0675` n `702`
- 4h: commodity avg `-0.0734` n `12`; crypto_alt avg `0.266` n `228`; crypto_major avg `-0.662` n `8`; equity avg `0.0475` n `78`; fx avg `-0.0078` n `6`; index avg `0.0209` n `23`; metal avg `0.0059` n `18`; unknown avg `-0.0959` n `654`
- 24h: commodity avg `0.082` n `12`; crypto_alt avg `1.2222` n `228`; crypto_major avg `-0.1679` n `8`; equity avg `0.3157` n `78`; fx avg `0.0444` n `6`; index avg `0.0497` n `23`; metal avg `-0.0254` n `18`; unknown avg `0.0885` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
