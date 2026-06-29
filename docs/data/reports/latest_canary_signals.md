# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T08:07:27.609424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.78` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.024` n `12`; crypto_alt avg `-0.1729` n `228`; crypto_major avg `-0.2638` n `8`; equity avg `0.138` n `88`; fx avg `-0.0053` n `6`; index avg `-0.0116` n `23`; metal avg `-0.0409` n `20`; unknown avg `1.5103` n `764`
- 1h: commodity avg `-0.1226` n `12`; crypto_alt avg `-0.0048` n `228`; crypto_major avg `-0.086` n `8`; equity avg `0.2859` n `88`; fx avg `0.0066` n `6`; index avg `0.0608` n `23`; metal avg `0.0274` n `20`; unknown avg `1.4352` n `764`
- 4h: commodity avg `-0.2135` n `12`; crypto_alt avg `-0.0299` n `228`; crypto_major avg `-0.1776` n `8`; equity avg `0.6097` n `88`; fx avg `0.0117` n `6`; index avg `0.1532` n `23`; metal avg `-0.0491` n `20`; unknown avg `1.533` n `732`
- 24h: commodity avg `-0.5569` n `12`; crypto_alt avg `0.187` n `228`; crypto_major avg `-0.0475` n `8`; equity avg `0.5691` n `88`; fx avg `0.049` n `6`; index avg `0.1005` n `23`; metal avg `-0.1671` n `20`; unknown avg `2.6431` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
