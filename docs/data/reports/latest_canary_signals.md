# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T13:37:28.725297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3839` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0133` n `13`; crypto_alt avg `0.0757` n `239`; crypto_major avg `0.0193` n `8`; equity avg `0.0042` n `162`; fx avg `0.0042` n `6`; index avg `0.0029` n `27`; metal avg `-0.0923` n `20`; unknown avg `0.2982` n `1261`
- 1h: commodity avg `0.36` n `13`; crypto_alt avg `-0.3362` n `239`; crypto_major avg `-0.4632` n `8`; equity avg `-0.5407` n `162`; fx avg `0.0304` n `6`; index avg `-0.0588` n `27`; metal avg `-0.1676` n `20`; unknown avg `0.4326` n `1253`
- 4h: commodity avg `0.2695` n `13`; crypto_alt avg `-1.1621` n `239`; crypto_major avg `-1.4938` n `8`; equity avg `-1.6589` n `162`; fx avg `-0.0042` n `6`; index avg `-0.1099` n `27`; metal avg `-0.2672` n `20`; unknown avg `20.1035` n `1247`
- 24h: commodity avg `0.1791` n `13`; crypto_alt avg `-3.1831` n `239`; crypto_major avg `-2.3503` n `8`; equity avg `-2.4813` n `162`; fx avg `-0.0652` n `6`; index avg `-0.1577` n `27`; metal avg `-1.0912` n `20`; unknown avg `0.1898` n `1138`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
