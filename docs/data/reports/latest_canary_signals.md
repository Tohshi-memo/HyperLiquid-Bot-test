# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T00:37:17.096545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0348` n `12`; crypto_alt avg `0.2506` n `228`; crypto_major avg `0.226` n `8`; equity avg `0.4308` n `66`; fx avg `-0.0` n `6`; index avg `0.2897` n `23`; metal avg `0.4181` n `18`; unknown avg `0.1091` n `384`
- 1h: commodity avg `-0.0864` n `12`; crypto_alt avg `-0.1943` n `228`; crypto_major avg `-0.5099` n `8`; equity avg `-0.3702` n `66`; fx avg `0.0376` n `6`; index avg `-0.179` n `23`; metal avg `0.0906` n `18`; unknown avg `-0.1854` n `383`
- 4h: commodity avg `-0.1506` n `12`; crypto_alt avg `-0.45` n `228`; crypto_major avg `-0.533` n `8`; equity avg `-0.191` n `66`; fx avg `-0.0102` n `6`; index avg `-0.0104` n `23`; metal avg `0.3958` n `18`; unknown avg `-0.4111` n `383`
- 24h: commodity avg `0.7845` n `12`; crypto_alt avg `-1.6852` n `228`; crypto_major avg `-1.4097` n `8`; equity avg `-0.6772` n `66`; fx avg `-0.0091` n `6`; index avg `-0.8173` n `23`; metal avg `-2.6066` n `18`; unknown avg `0.5079` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
