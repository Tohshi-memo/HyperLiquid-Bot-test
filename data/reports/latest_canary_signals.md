# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T16:07:28.899252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.051` n `12`; crypto_alt avg `0.1129` n `228`; crypto_major avg `0.0799` n `8`; equity avg `0.3024` n `88`; fx avg `-0.007` n `6`; index avg `0.0199` n `23`; metal avg `-0.0165` n `20`; unknown avg `-0.025` n `765`
- 1h: commodity avg `-0.0623` n `12`; crypto_alt avg `0.4305` n `228`; crypto_major avg `0.5071` n `8`; equity avg `0.4753` n `88`; fx avg `-0.015` n `6`; index avg `0.0347` n `23`; metal avg `-0.1019` n `20`; unknown avg `0.0987` n `765`
- 4h: commodity avg `-0.0867` n `12`; crypto_alt avg `0.5176` n `228`; crypto_major avg `-0.0448` n `8`; equity avg `0.6092` n `88`; fx avg `0.0783` n `6`; index avg `0.207` n `23`; metal avg `-0.1052` n `20`; unknown avg `-0.16` n `765`
- 24h: commodity avg `0.1771` n `12`; crypto_alt avg `-1.4947` n `228`; crypto_major avg `-0.96` n `8`; equity avg `1.7638` n `88`; fx avg `0.1345` n `6`; index avg `0.3845` n `23`; metal avg `0.22` n `20`; unknown avg `7.9044` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
