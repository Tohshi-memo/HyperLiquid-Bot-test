# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T16:07:33.060853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0451` n `12`; crypto_alt avg `-0.1703` n `230`; crypto_major avg `-0.3333` n `8`; equity avg `-0.2358` n `94`; fx avg `-0.0189` n `6`; index avg `-0.0596` n `25`; metal avg `-0.0966` n `20`; unknown avg `-0.1166` n `768`
- 1h: commodity avg `0.0481` n `12`; crypto_alt avg `0.1977` n `230`; crypto_major avg `-0.0139` n `8`; equity avg `-0.2924` n `94`; fx avg `-0.0254` n `6`; index avg `-0.0073` n `25`; metal avg `0.0271` n `20`; unknown avg `-0.0862` n `768`
- 4h: commodity avg `-0.2673` n `12`; crypto_alt avg `0.5037` n `230`; crypto_major avg `0.0345` n `8`; equity avg `-1.3267` n `94`; fx avg `-0.0539` n `6`; index avg `-0.0104` n `25`; metal avg `-0.2654` n `20`; unknown avg `-0.1146` n `768`
- 24h: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.4588` n `230`; crypto_major avg `-1.3874` n `8`; equity avg `-2.2917` n `94`; fx avg `-0.0897` n `6`; index avg `-0.1662` n `25`; metal avg `-0.2472` n `20`; unknown avg `-0.2387` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
