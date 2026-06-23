# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T00:22:26.574741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0145` n `12`; crypto_alt avg `-0.1226` n `228`; crypto_major avg `-0.109` n `8`; equity avg `-0.4127` n `86`; fx avg `-0.0101` n `6`; index avg `-0.1256` n `23`; metal avg `-0.1378` n `20`; unknown avg `-0.5283` n `716`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.115` n `228`; crypto_major avg `-0.1021` n `8`; equity avg `-0.5197` n `86`; fx avg `0.0242` n `6`; index avg `-0.1825` n `23`; metal avg `-0.2259` n `20`; unknown avg `-0.3179` n `716`
- 4h: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.995` n `228`; crypto_major avg `-0.7179` n `8`; equity avg `-0.8466` n `86`; fx avg `0.0077` n `6`; index avg `-0.219` n `23`; metal avg `-0.2183` n `20`; unknown avg `-0.391` n `716`
- 24h: commodity avg `-0.8444` n `12`; crypto_alt avg `-0.5799` n `228`; crypto_major avg `-0.1553` n `8`; equity avg `-0.5067` n `85`; fx avg `0.1041` n `6`; index avg `0.0478` n `23`; metal avg `-0.0565` n `18`; unknown avg `0.2041` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
