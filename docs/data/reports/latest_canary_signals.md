# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T05:07:25.399278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `-0.2985` n `231`; crypto_major avg `-0.3273` n `8`; equity avg `-0.0564` n `122`; fx avg `-0.0073` n `6`; index avg `-0.0067` n `25`; metal avg `0.0179` n `20`; unknown avg `7.732` n `797`
- 1h: commodity avg `0.0352` n `12`; crypto_alt avg `-0.4263` n `231`; crypto_major avg `-0.4705` n `8`; equity avg `-0.1052` n `122`; fx avg `0.0008` n `6`; index avg `-0.0133` n `25`; metal avg `-0.0198` n `20`; unknown avg `7.7926` n `797`
- 4h: commodity avg `0.0032` n `12`; crypto_alt avg `-0.1573` n `231`; crypto_major avg `-0.281` n `8`; equity avg `0.5488` n `122`; fx avg `-0.0269` n `6`; index avg `0.1556` n `25`; metal avg `0.0956` n `20`; unknown avg `7.8202` n `796`
- 24h: commodity avg `-0.7563` n `12`; crypto_alt avg `-3.2969` n `231`; crypto_major avg `-3.2097` n `8`; equity avg `1.1275` n `122`; fx avg `0.0296` n `6`; index avg `0.168` n `25`; metal avg `0.2352` n `20`; unknown avg `0.2124` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
