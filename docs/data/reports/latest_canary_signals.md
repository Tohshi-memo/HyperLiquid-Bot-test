# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T04:37:26.498970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `0.2033` n `228`; crypto_major avg `0.2513` n `8`; equity avg `0.1146` n `88`; fx avg `-0.0032` n `6`; index avg `0.053` n `23`; metal avg `0.2163` n `20`; unknown avg `5.9906` n `765`
- 1h: commodity avg `-0.0422` n `12`; crypto_alt avg `-0.0042` n `228`; crypto_major avg `-0.0462` n `8`; equity avg `0.2654` n `88`; fx avg `-0.0091` n `6`; index avg `0.1154` n `23`; metal avg `0.3188` n `20`; unknown avg `10.5507` n `765`
- 4h: commodity avg `0.0047` n `12`; crypto_alt avg `0.1485` n `228`; crypto_major avg `-0.087` n `8`; equity avg `0.9544` n `88`; fx avg `-0.0464` n `6`; index avg `0.2965` n `23`; metal avg `0.072` n `20`; unknown avg `11.5515` n `763`
- 24h: commodity avg `-0.2609` n `12`; crypto_alt avg `0.0996` n `228`; crypto_major avg `1.2552` n `8`; equity avg `2.5796` n `88`; fx avg `0.1138` n `6`; index avg `0.4905` n `23`; metal avg `-0.3204` n `20`; unknown avg `12.6794` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
