# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T23:52:23.122994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.043` n `12`; crypto_alt avg `0.1813` n `228`; crypto_major avg `0.1313` n `8`; equity avg `-0.0808` n `74`; fx avg `0.0034` n `6`; index avg `-0.1233` n `23`; metal avg `0.0075` n `18`; unknown avg `-0.0259` n `424`
- 1h: commodity avg `0.0594` n `12`; crypto_alt avg `0.6497` n `228`; crypto_major avg `0.5542` n `8`; equity avg `-0.2917` n `74`; fx avg `0.0091` n `6`; index avg `-0.1696` n `23`; metal avg `-0.1335` n `18`; unknown avg `-0.1956` n `424`
- 4h: commodity avg `-0.0207` n `12`; crypto_alt avg `-1.7042` n `228`; crypto_major avg `-0.6407` n `8`; equity avg `-1.0233` n `74`; fx avg `0.0149` n `6`; index avg `-0.4843` n `23`; metal avg `-0.2504` n `18`; unknown avg `-0.9318` n `424`
- 24h: commodity avg `-0.4989` n `12`; crypto_alt avg `-6.0842` n `228`; crypto_major avg `-3.6068` n `8`; equity avg `-0.2866` n `73`; fx avg `0.0575` n `6`; index avg `0.0595` n `23`; metal avg `0.4041` n `18`; unknown avg `-1.4522` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
