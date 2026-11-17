# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T15:07:43.866856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `13`; crypto_alt avg `-0.4257` n `239`; crypto_major avg `-0.4842` n `8`; equity avg `-0.1061` n `162`; fx avg `-0.0036` n `6`; index avg `-0.0052` n `27`; metal avg `-0.0812` n `20`; unknown avg `0.5049` n `1260`
- 1h: commodity avg `0.0299` n `13`; crypto_alt avg `-0.6595` n `239`; crypto_major avg `-0.7974` n `8`; equity avg `-1.0927` n `162`; fx avg `-0.0015` n `6`; index avg `-0.093` n `27`; metal avg `-0.018` n `20`; unknown avg `2.6946` n `1262`
- 4h: commodity avg `0.1779` n `13`; crypto_alt avg `0.2358` n `239`; crypto_major avg `0.153` n `8`; equity avg `-0.1488` n `162`; fx avg `0.0364` n `6`; index avg `-0.0411` n `27`; metal avg `-0.0512` n `20`; unknown avg `3.4317` n `1214`
- 24h: commodity avg `-0.1149` n `13`; crypto_alt avg `0.8363` n `239`; crypto_major avg `0.9567` n `8`; equity avg `-1.3553` n `162`; fx avg `-0.0377` n `6`; index avg `-0.166` n `27`; metal avg `-0.1037` n `20`; unknown avg `12.7955` n `1103`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
