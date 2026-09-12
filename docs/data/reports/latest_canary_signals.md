# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T05:37:26.861674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.81` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0152` n `12`; crypto_alt avg `0.2146` n `233`; crypto_major avg `0.0801` n `8`; equity avg `-0.014` n `136`; fx avg `0.0005` n `6`; index avg `0.0004` n `26`; metal avg `-0.0005` n `20`; unknown avg `1.1764` n `836`
- 1h: commodity avg `-0.0331` n `12`; crypto_alt avg `-0.0196` n `233`; crypto_major avg `-0.1122` n `8`; equity avg `-0.0141` n `136`; fx avg `-0.0021` n `6`; index avg `-0.0004` n `26`; metal avg `0.0051` n `20`; unknown avg `0.8075` n `836`
- 4h: commodity avg `-0.0638` n `12`; crypto_alt avg `0.2516` n `233`; crypto_major avg `0.0193` n `8`; equity avg `-0.0858` n `136`; fx avg `-0.0033` n `6`; index avg `-0.0113` n `26`; metal avg `-0.0115` n `20`; unknown avg `0.4682` n `818`
- 24h: commodity avg `-0.4666` n `12`; crypto_alt avg `0.9648` n `233`; crypto_major avg `0.8435` n `8`; equity avg `0.7106` n `136`; fx avg `-0.1293` n `6`; index avg `0.242` n `26`; metal avg `0.0388` n `20`; unknown avg `1.2804` n `690`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
