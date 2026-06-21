# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T13:07:28.622626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.146` n `12`; crypto_alt avg `0.2049` n `228`; crypto_major avg `0.1339` n `8`; equity avg `0.0099` n `78`; fx avg `0.0234` n `6`; index avg `-0.0013` n `23`; metal avg `0.0078` n `18`; unknown avg `0.039` n `702`
- 1h: commodity avg `-0.1557` n `12`; crypto_alt avg `0.2284` n `228`; crypto_major avg `0.1271` n `8`; equity avg `0.0393` n `78`; fx avg `-0.0807` n `6`; index avg `-0.0185` n `23`; metal avg `0.0071` n `18`; unknown avg `0.1982` n `702`
- 4h: commodity avg `-0.0438` n `12`; crypto_alt avg `0.3908` n `228`; crypto_major avg `0.1166` n `8`; equity avg `0.0273` n `78`; fx avg `-0.0661` n `6`; index avg `-0.0054` n `23`; metal avg `-0.0264` n `18`; unknown avg `0.024` n `702`
- 24h: commodity avg `0.0643` n `12`; crypto_alt avg `1.6755` n `228`; crypto_major avg `-0.1628` n `8`; equity avg `0.3238` n `78`; fx avg `-0.0471` n `6`; index avg `0.0077` n `23`; metal avg `-0.0727` n `18`; unknown avg `0.5289` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
