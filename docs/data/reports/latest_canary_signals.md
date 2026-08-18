# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T11:46:12.434982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.0027` n `230`; crypto_major avg `0.0127` n `8`; equity avg `0.1532` n `114`; fx avg `0.0059` n `6`; index avg `0.0162` n `25`; metal avg `0.0259` n `20`; unknown avg `-0.0018` n `795`
- 1h: commodity avg `0.0957` n `12`; crypto_alt avg `0.2058` n `230`; crypto_major avg `0.2738` n `8`; equity avg `0.2617` n `114`; fx avg `0.0008` n `6`; index avg `0.0293` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.0264` n `795`
- 4h: commodity avg `0.0292` n `12`; crypto_alt avg `0.3667` n `230`; crypto_major avg `0.258` n `8`; equity avg `-0.5726` n `114`; fx avg `-0.0233` n `6`; index avg `-0.0505` n `25`; metal avg `-0.0237` n `20`; unknown avg `-0.0049` n `795`
- 24h: commodity avg `0.6376` n `12`; crypto_alt avg `-0.7969` n `230`; crypto_major avg `0.2131` n `8`; equity avg `-2.3051` n `114`; fx avg `-0.0383` n `6`; index avg `-0.5004` n `25`; metal avg `-0.1979` n `20`; unknown avg `-0.0131` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
