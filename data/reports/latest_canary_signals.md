# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T00:07:22.830387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `13`; crypto_alt avg `-0.0629` n `239`; crypto_major avg `-0.063` n `8`; equity avg `-0.0181` n `158`; fx avg `0.0195` n `6`; index avg `0.0107` n `27`; metal avg `-0.006` n `20`; unknown avg `-0.1485` n `1252`
- 1h: commodity avg `-0.0672` n `13`; crypto_alt avg `0.1979` n `239`; crypto_major avg `0.2193` n `8`; equity avg `0.097` n `158`; fx avg `0.0169` n `6`; index avg `0.0233` n `27`; metal avg `0.0022` n `20`; unknown avg `-0.0442` n `1250`
- 4h: commodity avg `-0.0131` n `13`; crypto_alt avg `-0.1492` n `239`; crypto_major avg `0.0656` n `8`; equity avg `0.0258` n `158`; fx avg `0.0007` n `6`; index avg `0.008` n `27`; metal avg `-0.0018` n `20`; unknown avg `0.1299` n `1200`
- 24h: commodity avg `-0.0052` n `13`; crypto_alt avg `-1.1833` n `239`; crypto_major avg `-0.5264` n `8`; equity avg `-0.0006` n `158`; fx avg `-0.0018` n `6`; index avg `0.0667` n `27`; metal avg `-0.0269` n `20`; unknown avg `160.4037` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
