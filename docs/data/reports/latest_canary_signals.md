# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T05:22:31.248336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0219` n `13`; crypto_alt avg `-0.2194` n `239`; crypto_major avg `-0.1874` n `8`; equity avg `-0.1655` n `164`; fx avg `-0.0163` n `6`; index avg `-0.0144` n `27`; metal avg `-0.0573` n `20`; unknown avg `12.3265` n `1264`
- 1h: commodity avg `0.0076` n `13`; crypto_alt avg `-0.3955` n `239`; crypto_major avg `-0.0205` n `8`; equity avg `-0.3588` n `164`; fx avg `-0.0053` n `6`; index avg `-0.0526` n `27`; metal avg `0.0201` n `20`; unknown avg `40.008` n `1260`
- 4h: commodity avg `-0.0345` n `13`; crypto_alt avg `0.3854` n `239`; crypto_major avg `0.6682` n `8`; equity avg `-0.2732` n `164`; fx avg `-0.0281` n `6`; index avg `0.0044` n `27`; metal avg `-0.1269` n `20`; unknown avg `3.0086` n `1237`
- 24h: commodity avg `0.1092` n `13`; crypto_alt avg `-0.0251` n `239`; crypto_major avg `-1.1686` n `8`; equity avg `-0.6911` n `164`; fx avg `-0.1048` n `6`; index avg `0.0348` n `27`; metal avg `-0.6069` n `20`; unknown avg `173.468` n `1113`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
