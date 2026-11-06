# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T09:07:27.534230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `13`; crypto_alt avg `0.2439` n `239`; crypto_major avg `0.3712` n `8`; equity avg `0.7513` n `158`; fx avg `-0.0106` n `6`; index avg `0.0711` n `27`; metal avg `0.0465` n `20`; unknown avg `30.8168` n `1250`
- 1h: commodity avg `-0.2505` n `13`; crypto_alt avg `0.2709` n `239`; crypto_major avg `0.4273` n `8`; equity avg `1.1007` n `158`; fx avg `-0.0037` n `6`; index avg `0.1564` n `27`; metal avg `0.2175` n `20`; unknown avg `27.662` n `1240`
- 4h: commodity avg `-0.1684` n `13`; crypto_alt avg `0.7994` n `239`; crypto_major avg `0.3973` n `8`; equity avg `1.0629` n `158`; fx avg `-0.0965` n `6`; index avg `0.1109` n `27`; metal avg `0.2639` n `20`; unknown avg `18.0757` n `1166`
- 24h: commodity avg `0.8253` n `13`; crypto_alt avg `-3.9662` n `239`; crypto_major avg `-5.5942` n `8`; equity avg `-4.7383` n `158`; fx avg `-0.0573` n `6`; index avg `-0.6276` n `27`; metal avg `-0.1893` n `20`; unknown avg `232.5409` n `1047`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2211`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
