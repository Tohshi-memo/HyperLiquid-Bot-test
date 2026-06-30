# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T15:22:32.477317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2579` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.0366` n `228`; crypto_major avg `0.0572` n `8`; equity avg `0.0861` n `88`; fx avg `0.003` n `6`; index avg `-0.0153` n `23`; metal avg `-0.1349` n `20`; unknown avg `-0.0736` n `765`
- 1h: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.6284` n `228`; crypto_major avg `-0.8502` n `8`; equity avg `-0.3811` n `88`; fx avg `0.0603` n `6`; index avg `-0.0105` n `23`; metal avg `-0.3829` n `20`; unknown avg `-0.303` n `765`
- 4h: commodity avg `0.1482` n `12`; crypto_alt avg `-0.5675` n `228`; crypto_major avg `-1.1064` n `8`; equity avg `0.0458` n `88`; fx avg `0.0931` n `6`; index avg `0.1515` n `23`; metal avg `-0.1888` n `20`; unknown avg `-0.2107` n `765`
- 24h: commodity avg `0.3534` n `12`; crypto_alt avg `-1.1379` n `228`; crypto_major avg `-0.6486` n `8`; equity avg `2.3115` n `88`; fx avg `0.1555` n `6`; index avg `0.4453` n `23`; metal avg `0.3329` n `20`; unknown avg `8.6101` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
