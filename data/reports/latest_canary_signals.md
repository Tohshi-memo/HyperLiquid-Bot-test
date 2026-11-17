# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T06:07:27.074530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `13`; crypto_alt avg `-0.162` n `239`; crypto_major avg `-0.1324` n `8`; equity avg `-0.2134` n `162`; fx avg `0.0114` n `6`; index avg `-0.0168` n `27`; metal avg `-0.0614` n `20`; unknown avg `-0.0297` n `1244`
- 1h: commodity avg `0.0331` n `13`; crypto_alt avg `-0.1552` n `239`; crypto_major avg `-0.2111` n `8`; equity avg `-0.4207` n `162`; fx avg `0.0295` n `6`; index avg `-0.0279` n `27`; metal avg `-0.0021` n `20`; unknown avg `0.0867` n `1242`
- 4h: commodity avg `-0.0826` n `13`; crypto_alt avg `0.4813` n `239`; crypto_major avg `0.3766` n `8`; equity avg `-0.4177` n `162`; fx avg `0.0033` n `6`; index avg `-0.0777` n `27`; metal avg `0.0573` n `20`; unknown avg `-0.2462` n `1220`
- 24h: commodity avg `-1.1896` n `13`; crypto_alt avg `0.9253` n `239`; crypto_major avg `1.5211` n `8`; equity avg `-2.3065` n `162`; fx avg `-0.0076` n `6`; index avg `-0.2443` n `27`; metal avg `0.0171` n `20`; unknown avg `562.6504` n `981`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
