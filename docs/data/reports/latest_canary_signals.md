# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T01:22:25.653388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.2452` n `228`; crypto_major avg `-0.1662` n `8`; equity avg `-0.152` n `74`; fx avg `-0.0082` n `6`; index avg `-0.0327` n `23`; metal avg `-0.0446` n `18`; unknown avg `-0.1383` n `556`
- 1h: commodity avg `0.1747` n `12`; crypto_alt avg `-0.4661` n `228`; crypto_major avg `-0.2892` n `8`; equity avg `-0.2715` n `74`; fx avg `-0.0526` n `6`; index avg `-0.1097` n `23`; metal avg `-0.4679` n `18`; unknown avg `-0.1599` n `556`
- 4h: commodity avg `-0.0929` n `12`; crypto_alt avg `-0.6429` n `228`; crypto_major avg `-0.3765` n `8`; equity avg `0.378` n `74`; fx avg `-0.0613` n `6`; index avg `0.1236` n `23`; metal avg `-0.2586` n `18`; unknown avg `-0.4956` n `556`
- 24h: commodity avg `-2.4778` n `12`; crypto_alt avg `2.7283` n `228`; crypto_major avg `2.9` n `8`; equity avg `3.5783` n `74`; fx avg `-0.0498` n `6`; index avg `2.0417` n `23`; metal avg `2.4399` n `18`; unknown avg `2.5679` n `530`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
