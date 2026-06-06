# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T18:18:58.900327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2835` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `0.1642` n `228`; crypto_major avg `0.065` n `8`; equity avg `-0.0143` n `74`; fx avg `-0.0003` n `6`; index avg `-0.0055` n `23`; metal avg `-0.0044` n `18`; unknown avg `-0.0184` n `515`
- 1h: commodity avg `0.0481` n `12`; crypto_alt avg `-0.292` n `228`; crypto_major avg `-0.4004` n `8`; equity avg `-0.1578` n `74`; fx avg `0.1281` n `6`; index avg `-0.0832` n `23`; metal avg `0.0118` n `18`; unknown avg `0.8987` n `515`
- 4h: commodity avg `0.136` n `12`; crypto_alt avg `-1.4655` n `228`; crypto_major avg `-1.3893` n `8`; equity avg `-0.2732` n `74`; fx avg `0.1867` n `6`; index avg `-0.1058` n `23`; metal avg `0.0518` n `18`; unknown avg `-1.3403` n `515`
- 24h: commodity avg `0.3771` n `12`; crypto_alt avg `-1.2023` n `228`; crypto_major avg `-0.8628` n `8`; equity avg `-1.1593` n `74`; fx avg `0.1382` n `6`; index avg `-0.6246` n `23`; metal avg `-0.6657` n `18`; unknown avg `0.7736` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
