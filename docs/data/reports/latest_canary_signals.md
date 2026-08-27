# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T03:22:27.183023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `0.0712` n `231`; crypto_major avg `0.0152` n `8`; equity avg `0.0553` n `126`; fx avg `-0.0034` n `6`; index avg `0.0057` n `25`; metal avg `0.0426` n `20`; unknown avg `-0.0095` n `793`
- 1h: commodity avg `0.0217` n `12`; crypto_alt avg `-0.2161` n `231`; crypto_major avg `-0.1069` n `8`; equity avg `0.211` n `126`; fx avg `0.0285` n `6`; index avg `0.0114` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.0226` n `793`
- 4h: commodity avg `0.0183` n `12`; crypto_alt avg `-0.2689` n `231`; crypto_major avg `-0.0924` n `8`; equity avg `-0.1503` n `126`; fx avg `-0.0457` n `6`; index avg `-0.0829` n `25`; metal avg `0.1306` n `20`; unknown avg `0.3518` n `793`
- 24h: commodity avg `0.493` n `12`; crypto_alt avg `0.0835` n `231`; crypto_major avg `0.3944` n `8`; equity avg `1.3745` n `126`; fx avg `-0.1216` n `6`; index avg `0.1928` n `25`; metal avg `-0.1814` n `20`; unknown avg `0.4172` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
