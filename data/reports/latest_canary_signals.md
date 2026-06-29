# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T07:37:29.389502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1025` n `12`; crypto_alt avg `0.1043` n `228`; crypto_major avg `0.0877` n `8`; equity avg `0.0134` n `88`; fx avg `0.0055` n `6`; index avg `0.0139` n `23`; metal avg `-0.0098` n `20`; unknown avg `0.0632` n `764`
- 1h: commodity avg `-0.2313` n `12`; crypto_alt avg `0.1186` n `228`; crypto_major avg `0.037` n `8`; equity avg `-0.0168` n `88`; fx avg `-0.0118` n `6`; index avg `0.0144` n `23`; metal avg `-0.0726` n `20`; unknown avg `-0.0221` n `764`
- 4h: commodity avg `-0.1842` n `12`; crypto_alt avg `0.0995` n `228`; crypto_major avg `0.0239` n `8`; equity avg `0.6056` n `88`; fx avg `0.019` n `6`; index avg `0.2313` n `23`; metal avg `-0.0998` n `20`; unknown avg `0.0764` n `732`
- 24h: commodity avg `-0.5541` n `12`; crypto_alt avg `0.5003` n `228`; crypto_major avg `0.2301` n `8`; equity avg `0.4655` n `88`; fx avg `0.0496` n `6`; index avg `0.1264` n `23`; metal avg `-0.1938` n `20`; unknown avg `1.1815` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
