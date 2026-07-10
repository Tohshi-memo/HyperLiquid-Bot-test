# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T22:22:23.585839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.0847` n `229`; crypto_major avg `-0.0725` n `8`; equity avg `-0.0131` n `92`; fx avg `-0.0015` n `6`; index avg `0.0006` n `25`; metal avg `0.0` n `20`; unknown avg `-0.0913` n `765`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `0.1848` n `229`; crypto_major avg `0.0729` n `8`; equity avg `-0.003` n `92`; fx avg `-0.0041` n `6`; index avg `-0.0014` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.1982` n `765`
- 4h: commodity avg `0.0471` n `12`; crypto_alt avg `0.282` n `229`; crypto_major avg `0.0142` n `8`; equity avg `-0.1329` n `92`; fx avg `-0.0115` n `6`; index avg `0.0126` n `25`; metal avg `0.0978` n `20`; unknown avg `-0.4644` n `765`
- 24h: commodity avg `-0.2317` n `12`; crypto_alt avg `0.9857` n `229`; crypto_major avg `0.7896` n `8`; equity avg `-0.6983` n `92`; fx avg `-0.1724` n `6`; index avg `0.0349` n `25`; metal avg `0.1551` n `20`; unknown avg `-0.2388` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
