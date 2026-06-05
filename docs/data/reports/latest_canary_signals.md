# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T01:07:23.629457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.152` n `12`; crypto_alt avg `-0.6731` n `228`; crypto_major avg `-0.4577` n `8`; equity avg `-0.2925` n `74`; fx avg `0.0246` n `6`; index avg `0.0215` n `23`; metal avg `-0.141` n `18`; unknown avg `0.976` n `424`
- 1h: commodity avg `-0.272` n `12`; crypto_alt avg `-0.7672` n `228`; crypto_major avg `-0.5887` n `8`; equity avg `-0.6797` n `74`; fx avg `0.1047` n `6`; index avg `-0.298` n `23`; metal avg `-0.3548` n `18`; unknown avg `0.1636` n `424`
- 4h: commodity avg `-0.3987` n `12`; crypto_alt avg `-2.2519` n `228`; crypto_major avg `-1.5644` n `8`; equity avg `-1.5815` n `74`; fx avg `0.0853` n `6`; index avg `-0.772` n `23`; metal avg `-0.6465` n `18`; unknown avg `0.0036` n `424`
- 24h: commodity avg `-0.6233` n `12`; crypto_alt avg `-6.1408` n `228`; crypto_major avg `-3.7007` n `8`; equity avg `-1.8355` n `73`; fx avg `0.184` n `6`; index avg `-0.5734` n `23`; metal avg `-0.1952` n `18`; unknown avg `-1.2795` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
