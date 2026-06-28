# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T13:03:46.812988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `-0.38` n `228`; crypto_major avg `-0.4216` n `8`; equity avg `-0.0642` n `88`; fx avg `-0.0039` n `6`; index avg `-0.0017` n `23`; metal avg `-0.0085` n `20`; unknown avg `-0.047` n `764`
- 1h: commodity avg `-0.0501` n `12`; crypto_alt avg `-0.5265` n `228`; crypto_major avg `-0.5204` n `8`; equity avg `-0.0387` n `88`; fx avg `-0.0049` n `6`; index avg `-0.0008` n `23`; metal avg `-0.0019` n `20`; unknown avg `-0.0317` n `764`
- 4h: commodity avg `0.0342` n `12`; crypto_alt avg `-0.6092` n `228`; crypto_major avg `-0.5177` n `8`; equity avg `-0.0839` n `88`; fx avg `0.0027` n `6`; index avg `0.0044` n `23`; metal avg `-0.005` n `20`; unknown avg `1.4648` n `750`
- 24h: commodity avg `0.1301` n `12`; crypto_alt avg `-0.5408` n `228`; crypto_major avg `-1.1713` n `8`; equity avg `-0.0035` n `88`; fx avg `-0.0025` n `6`; index avg `-0.0535` n `23`; metal avg `-0.0289` n `20`; unknown avg `15.5508` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2052`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
