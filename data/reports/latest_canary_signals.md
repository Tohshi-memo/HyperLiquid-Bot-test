# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T07:52:34.890265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.0055` n `228`; crypto_major avg `-0.012` n `8`; equity avg `0.0969` n `88`; fx avg `-0.0027` n `6`; index avg `0.0206` n `23`; metal avg `-0.0063` n `20`; unknown avg `5.3649` n `756`
- 1h: commodity avg `0.0504` n `12`; crypto_alt avg `0.3437` n `228`; crypto_major avg `0.3015` n `8`; equity avg `0.1553` n `88`; fx avg `0.0191` n `6`; index avg `0.028` n `23`; metal avg `-0.0204` n `20`; unknown avg `0.6814` n `756`
- 4h: commodity avg `0.1117` n `12`; crypto_alt avg `0.0394` n `228`; crypto_major avg `-0.0253` n `8`; equity avg `0.1356` n `88`; fx avg `0.0177` n `6`; index avg `0.0174` n `23`; metal avg `-0.0345` n `20`; unknown avg `-0.1258` n `724`
- 24h: commodity avg `0.2941` n `12`; crypto_alt avg `-0.4943` n `228`; crypto_major avg `-1.2132` n `8`; equity avg `0.035` n `88`; fx avg `0.0204` n `6`; index avg `-0.1124` n `23`; metal avg `-0.0457` n `20`; unknown avg `16.8018` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2177`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
