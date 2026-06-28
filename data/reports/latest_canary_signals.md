# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T15:52:32.938486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `12`; crypto_alt avg `0.1214` n `228`; crypto_major avg `0.1201` n `8`; equity avg `0.0094` n `88`; fx avg `0.0` n `6`; index avg `-0.0192` n `23`; metal avg `-0.0014` n `20`; unknown avg `2.2399` n `764`
- 1h: commodity avg `-0.0214` n `12`; crypto_alt avg `-0.0426` n `228`; crypto_major avg `0.0838` n `8`; equity avg `-0.0298` n `88`; fx avg `-0.0077` n `6`; index avg `-0.0185` n `23`; metal avg `-0.0115` n `20`; unknown avg `-0.2154` n `764`
- 4h: commodity avg `0.0513` n `12`; crypto_alt avg `0.342` n `228`; crypto_major avg `-0.0441` n `8`; equity avg `0.0274` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0072` n `23`; metal avg `-0.0476` n `20`; unknown avg `1.4516` n `764`
- 24h: commodity avg `0.2537` n `12`; crypto_alt avg `-0.5805` n `228`; crypto_major avg `-1.5914` n `8`; equity avg `-0.0082` n `88`; fx avg `0.0053` n `6`; index avg `-0.0861` n `23`; metal avg `-0.0848` n `20`; unknown avg `16.0817` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.185`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
