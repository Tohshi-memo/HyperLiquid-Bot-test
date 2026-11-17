# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T11:14:52.033505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `13`; crypto_alt avg `0.4269` n `239`; crypto_major avg `0.4241` n `8`; equity avg `0.6659` n `162`; fx avg `0.0051` n `6`; index avg `0.05` n `27`; metal avg `0.0224` n `20`; unknown avg `160.4919` n `1262`
- 1h: commodity avg `0.0436` n `13`; crypto_alt avg `0.2194` n `239`; crypto_major avg `0.1249` n `8`; equity avg `0.4762` n `162`; fx avg `-0.0015` n `6`; index avg `0.0518` n `27`; metal avg `0.0868` n `20`; unknown avg `160.8349` n `1258`
- 4h: commodity avg `0.2631` n `13`; crypto_alt avg `-0.3617` n `239`; crypto_major avg `-0.5365` n `8`; equity avg `-0.3321` n `162`; fx avg `-0.056` n `6`; index avg `-0.0208` n `27`; metal avg `-0.1115` n `20`; unknown avg `1.8425` n `1220`
- 24h: commodity avg `-0.781` n `13`; crypto_alt avg `0.1909` n `239`; crypto_major avg `0.1979` n `8`; equity avg `-2.7071` n `162`; fx avg `-0.0619` n `6`; index avg `-0.2769` n `27`; metal avg `-0.1868` n `20`; unknown avg `13.6564` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
