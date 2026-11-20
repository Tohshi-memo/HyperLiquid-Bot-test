# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T04:37:24.618016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4929` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0086` n `13`; crypto_alt avg `-0.514` n `239`; crypto_major avg `-0.6562` n `8`; equity avg `-0.2029` n `165`; fx avg `0.004` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0991` n `20`; unknown avg `160.1332` n `1256`
- 1h: commodity avg `0.0431` n `13`; crypto_alt avg `-0.8361` n `239`; crypto_major avg `-0.9362` n `8`; equity avg `-0.2179` n `165`; fx avg `0.0007` n `6`; index avg `-0.049` n `27`; metal avg `-0.1049` n `20`; unknown avg `0.9966` n `1246`
- 4h: commodity avg `-0.0169` n `13`; crypto_alt avg `-2.1583` n `239`; crypto_major avg `-1.5443` n `8`; equity avg `-0.7172` n `165`; fx avg `-0.0255` n `6`; index avg `-0.0514` n `27`; metal avg `-0.6595` n `20`; unknown avg `3.6371` n `1242`
- 24h: commodity avg `-0.0655` n `13`; crypto_alt avg `-4.061` n `239`; crypto_major avg `-3.0997` n `8`; equity avg `-5.9428` n `165`; fx avg `0.0226` n `6`; index avg `-0.5211` n `27`; metal avg `-1.762` n `20`; unknown avg `71.811` n `1165`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
