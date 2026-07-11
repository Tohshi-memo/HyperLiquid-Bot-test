# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T16:52:28.636717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `12`; crypto_alt avg `0.0615` n `230`; crypto_major avg `-0.0445` n `8`; equity avg `-0.0023` n `92`; fx avg `-0.0095` n `6`; index avg `-0.003` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0068` n `765`
- 1h: commodity avg `-0.03` n `12`; crypto_alt avg `0.1184` n `230`; crypto_major avg `-0.0372` n `8`; equity avg `0.0668` n `92`; fx avg `-0.018` n `6`; index avg `0.0007` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.1401` n `765`
- 4h: commodity avg `-0.0501` n `12`; crypto_alt avg `0.1662` n `230`; crypto_major avg `0.2275` n `8`; equity avg `-0.0167` n `92`; fx avg `-0.0319` n `6`; index avg `0.0181` n `25`; metal avg `-0.0121` n `20`; unknown avg `0.0669` n `765`
- 24h: commodity avg `0.078` n `12`; crypto_alt avg `0.7442` n `229`; crypto_major avg `0.2817` n `8`; equity avg `-0.0903` n `92`; fx avg `-0.0546` n `6`; index avg `0.0289` n `25`; metal avg `0.0414` n `20`; unknown avg `2.2978` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
