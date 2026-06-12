# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T09:52:28.295391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `0.0484` n `228`; crypto_major avg `-0.0082` n `8`; equity avg `-0.036` n `74`; fx avg `0.0193` n `6`; index avg `-0.064` n `23`; metal avg `0.01` n `18`; unknown avg `3.3244` n `643`
- 1h: commodity avg `0.0869` n `12`; crypto_alt avg `0.7895` n `228`; crypto_major avg `0.5927` n `8`; equity avg `0.4791` n `74`; fx avg `0.0219` n `6`; index avg `0.2576` n `23`; metal avg `0.3267` n `18`; unknown avg `0.2138` n `643`
- 4h: commodity avg `-0.8636` n `12`; crypto_alt avg `1.1328` n `228`; crypto_major avg `0.8212` n `8`; equity avg `0.6875` n `74`; fx avg `0.0086` n `6`; index avg `0.4014` n `23`; metal avg `0.8535` n `18`; unknown avg `0.4955` n `515`
- 24h: commodity avg `-2.5317` n `12`; crypto_alt avg `2.1435` n `228`; crypto_major avg `2.143` n `8`; equity avg `2.9483` n `74`; fx avg `0.0081` n `6`; index avg `1.6126` n `23`; metal avg `3.4253` n `18`; unknown avg `-0.3179` n `514`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
