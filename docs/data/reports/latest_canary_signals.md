# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T17:15:19.700780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.81` - Polymarket crypto volume is unusually high.
- 1h_crypto_metal_divergence: score `2.0342` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `1.7587` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0478` n `12`; crypto_alt avg `0.7745` n `228`; crypto_major avg `1.0111` n `8`; equity avg `0.2547` n `88`; fx avg `-0.0029` n `6`; index avg `0.0304` n `23`; metal avg `0.0012` n `20`; unknown avg `0.0181` n `765`
- 1h: commodity avg `0.0305` n `12`; crypto_alt avg `1.3404` n `228`; crypto_major avg `2.0162` n `8`; equity avg `0.6962` n `88`; fx avg `-0.0076` n `6`; index avg `0.0728` n `23`; metal avg `-0.018` n `20`; unknown avg `1.4461` n `765`
- 4h: commodity avg `0.1644` n `12`; crypto_alt avg `1.0188` n `228`; crypto_major avg `1.4504` n `8`; equity avg `0.8125` n `88`; fx avg `0.0302` n `6`; index avg `0.0979` n `23`; metal avg `-0.3083` n `20`; unknown avg `0.429` n `764`
- 24h: commodity avg `-0.5567` n `12`; crypto_alt avg `2.0508` n `228`; crypto_major avg `2.7489` n `8`; equity avg `1.412` n `88`; fx avg `0.1407` n `6`; index avg `0.1673` n `23`; metal avg `-0.6277` n `20`; unknown avg `3.9186` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
