# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T21:08:11.489702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.057` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0171` n `12`; crypto_alt avg `-0.2266` n `234`; crypto_major avg `-0.0814` n `8`; equity avg `0.0129` n `140`; fx avg `0.0134` n `6`; index avg `0.0367` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.5297` n `941`
- 1h: commodity avg `0.0474` n `12`; crypto_alt avg `-0.4613` n `234`; crypto_major avg `-0.298` n `8`; equity avg `0.0253` n `140`; fx avg `-0.0396` n `6`; index avg `0.027` n `26`; metal avg `-0.0011` n `20`; unknown avg `-0.0998` n `941`
- 4h: commodity avg `0.0731` n `12`; crypto_alt avg `-0.924` n `234`; crypto_major avg `-1.0187` n `8`; equity avg `0.0921` n `140`; fx avg `-0.041` n `6`; index avg `0.0383` n `26`; metal avg `0.0085` n `20`; unknown avg `155.9339` n `911`
- 24h: commodity avg `0.114` n `12`; crypto_alt avg `0.9306` n `234`; crypto_major avg `-0.2433` n `8`; equity avg `-0.014` n `140`; fx avg `-0.0903` n `6`; index avg `0.0296` n `26`; metal avg `-0.0013` n `20`; unknown avg `5.8434` n `820`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
