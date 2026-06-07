# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T19:37:22.583569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.4462` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.2047` n `12`; crypto_alt avg `-0.2843` n `228`; crypto_major avg `-0.2243` n `8`; equity avg `-0.1456` n `74`; fx avg `0.0012` n `6`; index avg `-0.0423` n `23`; metal avg `-0.0948` n `18`; unknown avg `-0.1784` n `516`
- 1h: commodity avg `0.2775` n `12`; crypto_alt avg `-1.7951` n `228`; crypto_major avg `-1.5647` n `8`; equity avg `-0.6318` n `74`; fx avg `0.0154` n `6`; index avg `-0.1185` n `23`; metal avg `-0.2506` n `18`; unknown avg `-0.4232` n `516`
- 4h: commodity avg `0.5671` n `12`; crypto_alt avg `-2.0054` n `228`; crypto_major avg `-1.1784` n `8`; equity avg `-0.7063` n `74`; fx avg `0.0108` n `6`; index avg `-0.2514` n `23`; metal avg `-0.2125` n `18`; unknown avg `-2.7678` n `516`
- 24h: commodity avg `0.8859` n `12`; crypto_alt avg `1.1465` n `228`; crypto_major avg `2.5033` n `8`; equity avg `1.0958` n `74`; fx avg `-0.0628` n `6`; index avg `0.2685` n `23`; metal avg `0.3321` n `18`; unknown avg `-4.5737` n `505`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
