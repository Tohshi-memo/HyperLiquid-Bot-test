# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T15:22:32.862557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.666` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6373` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0963` n `12`; crypto_alt avg `-0.2159` n `234`; crypto_major avg `-0.0504` n `8`; equity avg `0.0986` n `140`; fx avg `-0.0075` n `6`; index avg `0.0125` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.5404` n `944`
- 1h: commodity avg `0.0862` n `12`; crypto_alt avg `0.7874` n `234`; crypto_major avg `0.9015` n `8`; equity avg `0.8243` n `140`; fx avg `-0.0265` n `6`; index avg `0.0896` n `26`; metal avg `0.0644` n `20`; unknown avg `3.7777` n `942`
- 4h: commodity avg `0.1488` n `12`; crypto_alt avg `-2.6058` n `234`; crypto_major avg `-1.8053` n `8`; equity avg `-0.3673` n `140`; fx avg `-0.0316` n `6`; index avg `-0.1393` n `26`; metal avg `-0.168` n `20`; unknown avg `508.8382` n `898`
- 24h: commodity avg `0.3507` n `12`; crypto_alt avg `-0.6697` n `234`; crypto_major avg `-2.2651` n `8`; equity avg `-0.4325` n `140`; fx avg `0.0179` n `6`; index avg `-0.202` n `26`; metal avg `-0.5001` n `20`; unknown avg `16.6606` n `830`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2519`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
