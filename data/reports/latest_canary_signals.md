# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T22:37:27.769031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5725` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5408` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0426` n `12`; crypto_alt avg `-0.8304` n `228`; crypto_major avg `-0.5569` n `8`; equity avg `-0.1822` n `86`; fx avg `0.0125` n `6`; index avg `-0.0273` n `23`; metal avg `-0.0478` n `20`; unknown avg `-0.3126` n `716`
- 1h: commodity avg `0.0467` n `12`; crypto_alt avg `-0.9645` n `228`; crypto_major avg `-0.6244` n `8`; equity avg `-0.2198` n `86`; fx avg `0.0158` n `6`; index avg `-0.0308` n `23`; metal avg `-0.0303` n `20`; unknown avg `-0.1672` n `716`
- 4h: commodity avg `0.1188` n `12`; crypto_alt avg `-1.7776` n `228`; crypto_major avg `-1.5658` n `8`; equity avg `-0.6685` n `86`; fx avg `-0.0037` n `6`; index avg `-0.025` n `23`; metal avg `0.0067` n `20`; unknown avg `0.9737` n `708`
- 24h: commodity avg `-0.7853` n `12`; crypto_alt avg `-0.6537` n `228`; crypto_major avg `-0.1572` n `8`; equity avg `-0.544` n `85`; fx avg `0.0861` n `6`; index avg `0.1646` n `23`; metal avg `0.367` n `18`; unknown avg `0.3742` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
