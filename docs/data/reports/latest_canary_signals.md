# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T19:22:25.603131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2638` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1181` n `12`; crypto_alt avg `-0.3522` n `228`; crypto_major avg `-0.3774` n `8`; equity avg `-0.1572` n `74`; fx avg `0.0125` n `6`; index avg `0.0205` n `23`; metal avg `0.0115` n `18`; unknown avg `0.15` n `516`
- 1h: commodity avg `0.5857` n `12`; crypto_alt avg `-1.6697` n `228`; crypto_major avg `-1.3374` n `8`; equity avg `-0.4605` n `74`; fx avg `0.0149` n `6`; index avg `-0.0736` n `23`; metal avg `-0.1872` n `18`; unknown avg `-0.2753` n `516`
- 4h: commodity avg `0.7426` n `12`; crypto_alt avg `-1.5241` n `228`; crypto_major avg `-0.6607` n `8`; equity avg `-0.4731` n `74`; fx avg `0.011` n `6`; index avg `-0.083` n `23`; metal avg `-0.0853` n `18`; unknown avg `-2.6015` n `516`
- 24h: commodity avg `1.0124` n `12`; crypto_alt avg `1.2701` n `228`; crypto_major avg `2.5833` n `8`; equity avg `1.2667` n `74`; fx avg `-0.0717` n `6`; index avg `0.2949` n `23`; metal avg `0.4106` n `18`; unknown avg `-4.4019` n `505`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
