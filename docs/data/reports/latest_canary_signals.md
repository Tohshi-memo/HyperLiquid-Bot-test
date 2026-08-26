# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T06:22:11.618216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `-0.2005` n `231`; crypto_major avg `-0.3742` n `8`; equity avg `-0.0808` n `122`; fx avg `-0.0014` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0615` n `20`; unknown avg `-0.0307` n `797`
- 1h: commodity avg `0.0199` n `12`; crypto_alt avg `0.3426` n `231`; crypto_major avg `0.1993` n `8`; equity avg `-0.1842` n `122`; fx avg `0.006` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0703` n `20`; unknown avg `0.0817` n `781`
- 4h: commodity avg `0.0869` n `12`; crypto_alt avg `0.0245` n `231`; crypto_major avg `-0.0474` n `8`; equity avg `0.0403` n `122`; fx avg `0.0232` n `6`; index avg `0.0508` n `25`; metal avg `-0.1453` n `20`; unknown avg `0.6682` n `781`
- 24h: commodity avg `-0.5061` n `12`; crypto_alt avg `-2.8557` n `231`; crypto_major avg `-2.8926` n `8`; equity avg `0.4286` n `122`; fx avg `-0.0117` n `6`; index avg `0.0588` n `25`; metal avg `0.1035` n `20`; unknown avg `0.6017` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
