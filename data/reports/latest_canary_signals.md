# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T22:37:29.436675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4596` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0046` n `13`; crypto_alt avg `0.6485` n `239`; crypto_major avg `0.5836` n `8`; equity avg `0.1207` n `165`; fx avg `-0.0054` n `6`; index avg `0.0115` n `27`; metal avg `0.0254` n `20`; unknown avg `0.3777` n `1262`
- 1h: commodity avg `0.0017` n `13`; crypto_alt avg `0.8383` n `239`; crypto_major avg `0.9409` n `8`; equity avg `0.6856` n `165`; fx avg `-0.0061` n `6`; index avg `0.057` n `27`; metal avg `0.0811` n `20`; unknown avg `1.6521` n `1252`
- 4h: commodity avg `-0.0494` n `13`; crypto_alt avg `-0.7755` n `239`; crypto_major avg `-1.6604` n `8`; equity avg `-2.5586` n `165`; fx avg `-0.0471` n `6`; index avg `-0.2008` n `27`; metal avg `-0.4864` n `20`; unknown avg `3.5874` n `1228`
- 24h: commodity avg `0.0889` n `13`; crypto_alt avg `0.0348` n `239`; crypto_major avg `0.0881` n `8`; equity avg `-2.8476` n `165`; fx avg `-0.0397` n `6`; index avg `-0.1457` n `27`; metal avg `-0.8107` n `20`; unknown avg `7.022` n `1168`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
