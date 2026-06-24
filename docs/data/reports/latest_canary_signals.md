# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T14:52:32.920951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1656` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0853` n `12`; crypto_alt avg `-0.0593` n `228`; crypto_major avg `-0.1226` n `8`; equity avg `0.0596` n `86`; fx avg `-0.0198` n `6`; index avg `0.0283` n `23`; metal avg `-0.1924` n `20`; unknown avg `-0.0649` n `764`
- 1h: commodity avg `-0.0891` n `12`; crypto_alt avg `0.2019` n `228`; crypto_major avg `-0.2192` n `8`; equity avg `0.0359` n `86`; fx avg `-0.0393` n `6`; index avg `0.0496` n `23`; metal avg `-0.2606` n `20`; unknown avg `-0.096` n `764`
- 4h: commodity avg `-0.4075` n `12`; crypto_alt avg `-0.8183` n `228`; crypto_major avg `-1.1621` n `8`; equity avg `-1.0752` n `86`; fx avg `-0.0675` n `6`; index avg `0.0035` n `23`; metal avg `-0.8423` n `20`; unknown avg `0.155` n `764`
- 24h: commodity avg `-0.7139` n `12`; crypto_alt avg `-1.6187` n `228`; crypto_major avg `-1.6276` n `8`; equity avg `2.6039` n `86`; fx avg `-0.0123` n `6`; index avg `0.1065` n `23`; metal avg `-1.5483` n `20`; unknown avg `-0.4298` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
