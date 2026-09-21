# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T21:37:33.705139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0208` n `12`; crypto_alt avg `0.3486` n `234`; crypto_major avg `0.5802` n `8`; equity avg `0.0541` n `140`; fx avg `-0.0018` n `6`; index avg `-0.0128` n `26`; metal avg `0.0083` n `20`; unknown avg `-0.0518` n `944`
- 1h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.0696` n `234`; crypto_major avg `0.2688` n `8`; equity avg `0.0949` n `140`; fx avg `0.0032` n `6`; index avg `-0.0144` n `26`; metal avg `0.0067` n `20`; unknown avg `17.2334` n `942`
- 4h: commodity avg `-0.0459` n `12`; crypto_alt avg `0.7843` n `234`; crypto_major avg `1.2635` n `8`; equity avg `0.3695` n `140`; fx avg `0.0027` n `6`; index avg `0.0264` n `26`; metal avg `0.0988` n `20`; unknown avg `36.5758` n `852`
- 24h: commodity avg `-1.0194` n `12`; crypto_alt avg `4.3003` n `234`; crypto_major avg `6.7222` n `8`; equity avg `2.9069` n `140`; fx avg `-0.0512` n `6`; index avg `0.5855` n `26`; metal avg `0.0503` n `20`; unknown avg `12.2014` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
