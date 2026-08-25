# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T17:07:30.489841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.3876` n `231`; crypto_major avg `-0.3741` n `8`; equity avg `-0.0973` n `122`; fx avg `0.0055` n `6`; index avg `-0.0125` n `25`; metal avg `-0.0507` n `20`; unknown avg `-0.1835` n `795`
- 1h: commodity avg `0.0418` n `12`; crypto_alt avg `-0.3648` n `231`; crypto_major avg `-0.4029` n `8`; equity avg `-0.2596` n `122`; fx avg `-0.0061` n `6`; index avg `-0.023` n `25`; metal avg `-0.0488` n `20`; unknown avg `-0.1661` n `795`
- 4h: commodity avg `0.1311` n `12`; crypto_alt avg `-0.5429` n `231`; crypto_major avg `-0.2116` n `8`; equity avg `0.3202` n `122`; fx avg `-0.0047` n `6`; index avg `-0.0449` n `25`; metal avg `0.2417` n `20`; unknown avg `-0.2071` n `795`
- 24h: commodity avg `-0.5462` n `12`; crypto_alt avg `-1.2067` n `231`; crypto_major avg `-0.1565` n `8`; equity avg `1.3427` n `122`; fx avg `0.0442` n `6`; index avg `0.1674` n `25`; metal avg `-0.158` n `20`; unknown avg `-0.8767` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
