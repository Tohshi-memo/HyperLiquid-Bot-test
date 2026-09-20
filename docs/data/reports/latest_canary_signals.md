# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T03:07:29.272581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4515` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1712` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.0756` n `234`; crypto_major avg `-0.1221` n `8`; equity avg `-0.1178` n `140`; fx avg `0.0023` n `6`; index avg `-0.0322` n `26`; metal avg `-0.0301` n `20`; unknown avg `0.3906` n `941`
- 1h: commodity avg `0.0442` n `12`; crypto_alt avg `-1.7233` n `234`; crypto_major avg `-1.2411` n `8`; equity avg `-0.4094` n `140`; fx avg `-0.0001` n `6`; index avg `-0.0699` n `26`; metal avg `-0.0336` n `20`; unknown avg `4.8113` n `941`
- 4h: commodity avg `0.2928` n `12`; crypto_alt avg `-1.3886` n `234`; crypto_major avg `-1.5233` n `8`; equity avg `-0.3465` n `140`; fx avg `-0.0027` n `6`; index avg `-0.0718` n `26`; metal avg `-0.0386` n `20`; unknown avg `4.5701` n `919`
- 24h: commodity avg `0.2084` n `12`; crypto_alt avg `-1.2404` n `234`; crypto_major avg `-2.2839` n `8`; equity avg `-0.2695` n `140`; fx avg `-0.0563` n `6`; index avg `-0.0314` n `26`; metal avg `-0.0352` n `20`; unknown avg `5.7815` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
