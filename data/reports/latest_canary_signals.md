# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T23:22:27.117040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0591` n `13`; crypto_alt avg `0.2989` n `239`; crypto_major avg `0.3148` n `8`; equity avg `0.2856` n `164`; fx avg `0.0075` n `6`; index avg `0.0151` n `27`; metal avg `0.0667` n `20`; unknown avg `0.9083` n `1263`
- 1h: commodity avg `0.0374` n `13`; crypto_alt avg `0.4213` n `239`; crypto_major avg `0.4721` n `8`; equity avg `0.8055` n `164`; fx avg `0.0044` n `6`; index avg `0.0964` n `27`; metal avg `0.1312` n `20`; unknown avg `4.7443` n `1263`
- 4h: commodity avg `-0.0157` n `13`; crypto_alt avg `-0.1473` n `239`; crypto_major avg `-0.22` n `8`; equity avg `0.5553` n `164`; fx avg `0.0071` n `6`; index avg `0.0841` n `27`; metal avg `0.1295` n `20`; unknown avg `4.5901` n `1221`
- 24h: commodity avg `-0.2323` n `13`; crypto_alt avg `-1.5356` n `239`; crypto_major avg `-2.3329` n `8`; equity avg `-2.1176` n `164`; fx avg `-0.1526` n `6`; index avg `-0.1595` n `27`; metal avg `-1.0866` n `20`; unknown avg `87.7436` n `1128`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
