# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T10:52:30.994748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9588` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.0007` n `229`; crypto_major avg `0.2012` n `8`; equity avg `-0.022` n `88`; fx avg `0.0064` n `6`; index avg `-0.0256` n `25`; metal avg `-0.0365` n `20`; unknown avg `0.1012` n `763`
- 1h: commodity avg `-0.0058` n `12`; crypto_alt avg `0.0743` n `229`; crypto_major avg `0.5978` n `8`; equity avg `-0.0183` n `88`; fx avg `0.0193` n `6`; index avg `-0.0077` n `25`; metal avg `-0.0656` n `20`; unknown avg `0.0869` n `763`
- 4h: commodity avg `0.0028` n `12`; crypto_alt avg `1.3784` n `228`; crypto_major avg `1.9844` n `8`; equity avg `0.5567` n `88`; fx avg `-0.0091` n `6`; index avg `0.0391` n `25`; metal avg `0.0256` n `20`; unknown avg `1.3477` n `763`
- 24h: commodity avg `-0.4719` n `12`; crypto_alt avg `3.0102` n `228`; crypto_major avg `3.8782` n `8`; equity avg `-1.9516` n `88`; fx avg `-0.1184` n `6`; index avg `-0.5554` n `25`; metal avg `1.0429` n `20`; unknown avg `3.4021` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
