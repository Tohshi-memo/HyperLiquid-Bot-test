# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T10:07:25.772785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.79` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1915` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0509` n `12`; crypto_alt avg `0.0294` n `228`; crypto_major avg `0.1722` n `8`; equity avg `-0.034` n `69`; fx avg `0.0029` n `6`; index avg `-0.0082` n `23`; metal avg `-0.0336` n `18`; unknown avg `-0.0341` n `422`
- 1h: commodity avg `0.0445` n `12`; crypto_alt avg `-0.4096` n `228`; crypto_major avg `-0.2882` n `8`; equity avg `0.0949` n `69`; fx avg `0.012` n `6`; index avg `0.0058` n `23`; metal avg `-0.1044` n `18`; unknown avg `-0.2447` n `422`
- 4h: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.6696` n `228`; crypto_major avg `-0.9438` n `8`; equity avg `0.2642` n `69`; fx avg `0.0477` n `6`; index avg `0.2477` n `23`; metal avg `-0.1001` n `18`; unknown avg `-0.8359` n `422`
- 24h: commodity avg `-1.1518` n `12`; crypto_alt avg `-0.5173` n `228`; crypto_major avg `-2.1486` n `8`; equity avg `0.6562` n `69`; fx avg `0.122` n `6`; index avg `0.0761` n `23`; metal avg `0.8314` n `18`; unknown avg `0.2703` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
