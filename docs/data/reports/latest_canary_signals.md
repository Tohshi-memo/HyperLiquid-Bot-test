# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T05:07:34.657208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2279` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.3774` n `234`; crypto_major avg `-0.1791` n `8`; equity avg `0.0009` n `141`; fx avg `0.0133` n `6`; index avg `0.0087` n `26`; metal avg `-0.0262` n `20`; unknown avg `25.3831` n `960`
- 1h: commodity avg `0.0198` n `12`; crypto_alt avg `0.2455` n `234`; crypto_major avg `0.1634` n `8`; equity avg `0.1206` n `141`; fx avg `0.0275` n `6`; index avg `0.037` n `26`; metal avg `-0.0395` n `20`; unknown avg `23.8463` n `960`
- 4h: commodity avg `0.2239` n `12`; crypto_alt avg `-2.3491` n `234`; crypto_major avg `-1.2942` n `8`; equity avg `-0.8772` n `141`; fx avg `0.0196` n `6`; index avg `-0.0663` n `26`; metal avg `-0.2576` n `20`; unknown avg `214.2994` n `936`
- 24h: commodity avg `-0.324` n `12`; crypto_alt avg `-1.2964` n `234`; crypto_major avg `-1.2069` n `8`; equity avg `-1.4022` n `141`; fx avg `0.0648` n `6`; index avg `-0.135` n `26`; metal avg `-0.7283` n `20`; unknown avg `6.183` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
