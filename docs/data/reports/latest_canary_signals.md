# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T02:52:31.599435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4703` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0441` n `12`; crypto_alt avg `-0.328` n `231`; crypto_major avg `-0.4059` n `8`; equity avg `-0.1174` n `128`; fx avg `0.007` n `6`; index avg `-0.0038` n `26`; metal avg `0.0517` n `20`; unknown avg `0.1095` n `793`
- 1h: commodity avg `0.0276` n `12`; crypto_alt avg `-0.0767` n `231`; crypto_major avg `-0.1613` n `8`; equity avg `-0.1117` n `128`; fx avg `-0.0039` n `6`; index avg `0.0212` n `26`; metal avg `-0.0911` n `20`; unknown avg `-0.3288` n `791`
- 4h: commodity avg `0.0847` n `12`; crypto_alt avg `-1.3491` n `231`; crypto_major avg `-1.6661` n `8`; equity avg `-1.1256` n `128`; fx avg `-0.0466` n `6`; index avg `-0.1958` n `26`; metal avg `-0.3513` n `20`; unknown avg `1.8908` n `779`
- 24h: commodity avg `0.3965` n `12`; crypto_alt avg `-0.9487` n `231`; crypto_major avg `-2.5047` n `8`; equity avg `-1.4201` n `128`; fx avg `-0.032` n `6`; index avg `-0.2882` n `26`; metal avg `-0.4233` n `20`; unknown avg `-0.531` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
