# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T13:52:32.158811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.347` n `12`; crypto_alt avg `-0.3697` n `228`; crypto_major avg `-0.1157` n `8`; equity avg `-0.3027` n `74`; fx avg `-0.0078` n `6`; index avg `-0.3703` n `23`; metal avg `-0.2332` n `18`; unknown avg `0.1099` n `643`
- 1h: commodity avg `0.51` n `12`; crypto_alt avg `-0.9911` n `228`; crypto_major avg `-0.4696` n `8`; equity avg `-0.9491` n `74`; fx avg `0.0106` n `6`; index avg `-0.4308` n `23`; metal avg `-0.093` n `18`; unknown avg `-0.0307` n `643`
- 4h: commodity avg `1.2965` n `12`; crypto_alt avg `-1.1749` n `228`; crypto_major avg `-0.5297` n `8`; equity avg `-1.6124` n `74`; fx avg `-0.014` n `6`; index avg `-0.6408` n `23`; metal avg `-0.9229` n `18`; unknown avg `1.6825` n `643`
- 24h: commodity avg `-1.2317` n `12`; crypto_alt avg `0.8086` n `228`; crypto_major avg `1.2578` n `8`; equity avg `1.0484` n `74`; fx avg `0.0152` n `6`; index avg `0.8347` n `23`; metal avg `2.1386` n `18`; unknown avg `1.4943` n `514`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
