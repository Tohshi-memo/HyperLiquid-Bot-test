# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T11:28:28.969177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `12`; crypto_alt avg `0.1828` n `228`; crypto_major avg `0.2635` n `8`; equity avg `0.0501` n `88`; fx avg `-0.0093` n `6`; index avg `0.0175` n `23`; metal avg `0.004` n `20`; unknown avg `-0.0254` n `764`
- 1h: commodity avg `0.038` n `12`; crypto_alt avg `0.2457` n `228`; crypto_major avg `0.351` n `8`; equity avg `0.0752` n `88`; fx avg `-0.0017` n `6`; index avg `0.0201` n `23`; metal avg `0.0019` n `20`; unknown avg `-0.3645` n `764`
- 4h: commodity avg `-0.0926` n `12`; crypto_alt avg `0.4034` n `228`; crypto_major avg `0.5755` n `8`; equity avg `0.2489` n `88`; fx avg `0.0141` n `6`; index avg `0.0722` n `23`; metal avg `0.0224` n `20`; unknown avg `2.3482` n `742`
- 24h: commodity avg `0.1815` n `12`; crypto_alt avg `0.2573` n `228`; crypto_major avg `-0.3245` n `8`; equity avg `0.1542` n `88`; fx avg `-0.0082` n `6`; index avg `-0.0296` n `23`; metal avg `-0.0068` n `20`; unknown avg `19.543` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2126`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
