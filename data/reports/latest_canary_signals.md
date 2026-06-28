# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T15:22:29.304662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.1615` n `228`; crypto_major avg `-0.0598` n `8`; equity avg `-0.0056` n `88`; fx avg `0.005` n `6`; index avg `0.001` n `23`; metal avg `-0.0047` n `20`; unknown avg `0.0297` n `764`
- 1h: commodity avg `0.0223` n `12`; crypto_alt avg `0.0074` n `228`; crypto_major avg `-0.176` n `8`; equity avg `-0.0119` n `88`; fx avg `0.011` n `6`; index avg `0.0132` n `23`; metal avg `-0.0311` n `20`; unknown avg `2.4599` n `764`
- 4h: commodity avg `0.0882` n `12`; crypto_alt avg `0.3223` n `228`; crypto_major avg `-0.1569` n `8`; equity avg `-0.0043` n `88`; fx avg `0.0068` n `6`; index avg `0.0102` n `23`; metal avg `-0.0496` n `20`; unknown avg `2.6429` n `764`
- 24h: commodity avg `0.2026` n `12`; crypto_alt avg `-0.3688` n `228`; crypto_major avg `-1.6093` n `8`; equity avg `-0.0015` n `88`; fx avg `-0.0017` n `6`; index avg `-0.0521` n `23`; metal avg `-0.0742` n `20`; unknown avg `16.3038` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1948`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.185`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
