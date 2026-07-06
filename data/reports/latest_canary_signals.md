# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T12:37:29.542485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0558` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0243` n `12`; crypto_alt avg `0.1627` n `229`; crypto_major avg `0.0046` n `8`; equity avg `-0.0723` n `88`; fx avg `0.0099` n `6`; index avg `-0.0115` n `25`; metal avg `-0.1243` n `20`; unknown avg `0.0952` n `765`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.9439` n `229`; crypto_major avg `-1.0509` n `8`; equity avg `-0.1178` n `88`; fx avg `0.0147` n `6`; index avg `0.0049` n `25`; metal avg `-0.2419` n `20`; unknown avg `0.0049` n `765`
- 4h: commodity avg `0.0244` n `12`; crypto_alt avg `-0.4681` n `229`; crypto_major avg `-0.7116` n `8`; equity avg `-0.1431` n `88`; fx avg `0.0016` n `6`; index avg `0.0174` n `25`; metal avg `-0.1656` n `20`; unknown avg `-0.0953` n `765`
- 24h: commodity avg `-0.1595` n `12`; crypto_alt avg `-0.9191` n `229`; crypto_major avg `-0.629` n `8`; equity avg `-0.8831` n `88`; fx avg `0.1099` n `6`; index avg `-0.006` n `25`; metal avg `-0.3965` n `20`; unknown avg `0.7566` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
