# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T20:07:23.973406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3695` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `-0.0442` n `231`; crypto_major avg `-0.1177` n `8`; equity avg `-0.05` n `127`; fx avg `-0.0019` n `6`; index avg `-0.016` n `26`; metal avg `0.0252` n `20`; unknown avg `0.066` n `793`
- 1h: commodity avg `0.0202` n `12`; crypto_alt avg `0.1248` n `231`; crypto_major avg `-0.0485` n `8`; equity avg `0.0351` n `127`; fx avg `-0.0032` n `6`; index avg `-0.0121` n `26`; metal avg `-0.0019` n `20`; unknown avg `-0.241` n `793`
- 4h: commodity avg `0.083` n `12`; crypto_alt avg `-1.0037` n `231`; crypto_major avg `-1.4875` n `8`; equity avg `-0.4516` n `127`; fx avg `-0.0276` n `6`; index avg `-0.118` n `26`; metal avg `-0.3907` n `20`; unknown avg `0.1056` n `793`
- 24h: commodity avg `-0.1543` n `12`; crypto_alt avg `-3.3098` n `231`; crypto_major avg `-3.7762` n `8`; equity avg `-2.5173` n `127`; fx avg `-0.1228` n `6`; index avg `-0.2218` n `26`; metal avg `-0.3866` n `20`; unknown avg `-0.6651` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
