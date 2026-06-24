# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T10:22:33.710537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `-0.3037` n `228`; crypto_major avg `-0.1953` n `8`; equity avg `0.0415` n `86`; fx avg `-0.0301` n `6`; index avg `0.0219` n `23`; metal avg `-0.0823` n `20`; unknown avg `-0.0028` n `764`
- 1h: commodity avg `0.1128` n `12`; crypto_alt avg `-0.3169` n `228`; crypto_major avg `-0.2267` n `8`; equity avg `-0.0328` n `86`; fx avg `-0.0458` n `6`; index avg `0.0246` n `23`; metal avg `-0.2461` n `20`; unknown avg `-0.082` n `764`
- 4h: commodity avg `-0.0431` n `12`; crypto_alt avg `-0.4326` n `228`; crypto_major avg `-0.5887` n `8`; equity avg `-0.1297` n `86`; fx avg `-0.0158` n `6`; index avg `0.0284` n `23`; metal avg `-0.5428` n `20`; unknown avg `-0.4229` n `756`
- 24h: commodity avg `-0.4582` n `12`; crypto_alt avg `-0.1628` n `228`; crypto_major avg `-0.1356` n `8`; equity avg `4.6516` n `86`; fx avg `-0.0139` n `6`; index avg `0.0785` n `23`; metal avg `-0.8299` n `20`; unknown avg `-0.0369` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
