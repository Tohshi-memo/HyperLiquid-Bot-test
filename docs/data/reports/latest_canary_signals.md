# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T03:37:42.054801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2212` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0538` n `12`; crypto_alt avg `-0.4476` n `234`; crypto_major avg `-0.1476` n `8`; equity avg `-0.1198` n `141`; fx avg `-0.0071` n `6`; index avg `-0.0205` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.2817` n `960`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `-1.1532` n `234`; crypto_major avg `-0.3074` n `8`; equity avg `-0.2624` n `141`; fx avg `-0.0096` n `6`; index avg `-0.0297` n `26`; metal avg `-0.0562` n `20`; unknown avg `0.5221` n `952`
- 4h: commodity avg `-0.0356` n `12`; crypto_alt avg `-2.1482` n `234`; crypto_major avg `-1.3457` n `8`; equity avg `-1.4699` n `141`; fx avg `0.076` n `6`; index avg `-0.1245` n `26`; metal avg `-0.5364` n `20`; unknown avg `141.7729` n `936`
- 24h: commodity avg `-0.4097` n `12`; crypto_alt avg `-1.4036` n `234`; crypto_major avg `-1.3864` n `8`; equity avg `-1.568` n `141`; fx avg `0.0613` n `6`; index avg `-0.1667` n `26`; metal avg `-0.7241` n `20`; unknown avg `12.9416` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
