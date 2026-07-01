# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T08:46:19.182004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3408` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `0.1283` n `228`; crypto_major avg `0.2063` n `8`; equity avg `0.0734` n `88`; fx avg `0.0032` n `6`; index avg `0.0088` n `23`; metal avg `0.047` n `20`; unknown avg `0.0082` n `765`
- 1h: commodity avg `-0.2061` n `12`; crypto_alt avg `-0.032` n `228`; crypto_major avg `-0.2707` n `8`; equity avg `0.0129` n `88`; fx avg `-0.0148` n `6`; index avg `0.0132` n `23`; metal avg `0.0579` n `20`; unknown avg `0.2189` n `765`
- 4h: commodity avg `-0.2957` n `12`; crypto_alt avg `-1.2161` n `228`; crypto_major avg `-1.4234` n `8`; equity avg `-0.4371` n `88`; fx avg `0.0292` n `6`; index avg `-0.0826` n `23`; metal avg `-0.0765` n `20`; unknown avg `-0.2277` n `743`
- 24h: commodity avg `-0.3921` n `12`; crypto_alt avg `-0.4397` n `228`; crypto_major avg `-0.5567` n `8`; equity avg `0.6548` n `88`; fx avg `0.084` n `6`; index avg `0.0164` n `23`; metal avg `-0.5796` n `20`; unknown avg `-0.2249` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
