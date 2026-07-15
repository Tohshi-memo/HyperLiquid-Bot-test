# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T06:22:26.781336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0675` n `12`; crypto_alt avg `-0.09` n `230`; crypto_major avg `0.0165` n `8`; equity avg `-0.1353` n `93`; fx avg `-0.0042` n `6`; index avg `-0.0506` n `25`; metal avg `-0.072` n `20`; unknown avg `-0.0086` n `767`
- 1h: commodity avg `-0.0772` n `12`; crypto_alt avg `0.3886` n `230`; crypto_major avg `0.6376` n `8`; equity avg `0.1304` n `93`; fx avg `-0.0196` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0249` n `20`; unknown avg `0.0236` n `749`
- 4h: commodity avg `-0.1427` n `12`; crypto_alt avg `0.2798` n `230`; crypto_major avg `1.0045` n `8`; equity avg `0.3489` n `93`; fx avg `-0.0058` n `6`; index avg `0.0097` n `25`; metal avg `-0.0505` n `20`; unknown avg `0.1936` n `749`
- 24h: commodity avg `-0.0147` n `12`; crypto_alt avg `1.6187` n `230`; crypto_major avg `3.4789` n `8`; equity avg `1.7748` n `92`; fx avg `0.0609` n `6`; index avg `0.477` n `25`; metal avg `0.1654` n `20`; unknown avg `0.2899` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
