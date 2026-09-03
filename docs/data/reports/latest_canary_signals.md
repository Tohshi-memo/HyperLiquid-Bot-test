# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T03:52:37.727560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.0254` n `232`; crypto_major avg `0.0774` n `8`; equity avg `0.0173` n `133`; fx avg `-0.0254` n `6`; index avg `-0.0012` n `26`; metal avg `0.003` n `20`; unknown avg `15.8959` n `792`
- 1h: commodity avg `-0.008` n `12`; crypto_alt avg `-0.3195` n `232`; crypto_major avg `-0.2423` n `8`; equity avg `0.2104` n `133`; fx avg `-0.0226` n `6`; index avg `0.0366` n `26`; metal avg `0.0926` n `20`; unknown avg `-0.0009` n `790`
- 4h: commodity avg `0.0507` n `12`; crypto_alt avg `0.6793` n `232`; crypto_major avg `0.6137` n `8`; equity avg `0.2632` n `133`; fx avg `-0.1122` n `6`; index avg `0.0009` n `26`; metal avg `0.2163` n `20`; unknown avg `0.1123` n `790`
- 24h: commodity avg `0.182` n `12`; crypto_alt avg `0.4022` n `232`; crypto_major avg `0.3385` n `8`; equity avg `1.6244` n `133`; fx avg `-0.4024` n `6`; index avg `0.2037` n `26`; metal avg `0.9449` n `20`; unknown avg `-0.3258` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
