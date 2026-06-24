# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T15:37:30.115709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.2673` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.0406` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.6747` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.1356` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0661` n `12`; crypto_alt avg `-0.6025` n `228`; crypto_major avg `-0.8179` n `8`; equity avg `-0.0844` n `86`; fx avg `-0.0105` n `6`; index avg `0.0212` n `23`; metal avg `-0.0339` n `20`; unknown avg `-0.2459` n `764`
- 1h: commodity avg `0.0904` n `12`; crypto_alt avg `-0.846` n `228`; crypto_major avg `-1.1266` n `8`; equity avg `-0.0529` n `86`; fx avg `0.0198` n `6`; index avg `0.009` n `23`; metal avg `-0.17` n `20`; unknown avg `-0.3084` n `764`
- 4h: commodity avg `-0.2271` n `12`; crypto_alt avg `-1.5544` n `228`; crypto_major avg `-2.2677` n `8`; equity avg `-1.1913` n `86`; fx avg `-0.0283` n `6`; index avg `-0.0004` n `23`; metal avg `-0.593` n `20`; unknown avg `-0.0362` n `764`
- 24h: commodity avg `-0.5435` n `12`; crypto_alt avg `-1.7643` n `228`; crypto_major avg `-1.9678` n `8`; equity avg `2.9887` n `86`; fx avg `0.0415` n `6`; index avg `0.1832` n `23`; metal avg `-1.6152` n `20`; unknown avg `-0.2223` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
