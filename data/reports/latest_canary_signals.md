# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T09:22:27.015997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `0.5259` n `228`; crypto_major avg `0.3618` n `8`; equity avg `0.0607` n `74`; fx avg `-0.0159` n `6`; index avg `0.1242` n `23`; metal avg `0.0563` n `18`; unknown avg `-0.0334` n `517`
- 1h: commodity avg `-0.0579` n `12`; crypto_alt avg `0.4859` n `228`; crypto_major avg `0.4979` n `8`; equity avg `-0.0096` n `74`; fx avg `-0.0298` n `6`; index avg `0.0335` n `23`; metal avg `0.0308` n `18`; unknown avg `0.1392` n `517`
- 4h: commodity avg `0.0128` n `12`; crypto_alt avg `1.0194` n `228`; crypto_major avg `0.7491` n `8`; equity avg `0.5456` n `74`; fx avg `-0.1802` n `6`; index avg `0.2547` n `23`; metal avg `-0.2078` n `18`; unknown avg `-0.2645` n `507`
- 24h: commodity avg `0.8689` n `12`; crypto_alt avg `-0.47` n `228`; crypto_major avg `0.5806` n `8`; equity avg `0.6852` n `74`; fx avg `-0.3306` n `6`; index avg `0.2328` n `23`; metal avg `-0.9092` n `18`; unknown avg `-4.7125` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
