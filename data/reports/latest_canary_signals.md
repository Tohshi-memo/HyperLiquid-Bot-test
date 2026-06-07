# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T19:07:19.894188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3934` n `12`; crypto_alt avg `-0.932` n `228`; crypto_major avg `-0.7007` n `8`; equity avg `-0.2571` n `74`; fx avg `0.0031` n `6`; index avg `-0.0198` n `23`; metal avg `-0.1142` n `18`; unknown avg `-0.1203` n `516`
- 1h: commodity avg `0.5403` n `12`; crypto_alt avg `-1.473` n `228`; crypto_major avg `-1.0064` n `8`; equity avg `-0.4148` n `74`; fx avg `-0.0054` n `6`; index avg `-0.1787` n `23`; metal avg `-0.2188` n `18`; unknown avg `-0.2263` n `516`
- 4h: commodity avg `0.6974` n `12`; crypto_alt avg `-1.2071` n `228`; crypto_major avg `-0.0737` n `8`; equity avg `-0.3112` n `74`; fx avg `-0.0021` n `6`; index avg `-0.1355` n `23`; metal avg `-0.0753` n `18`; unknown avg `-2.579` n `516`
- 24h: commodity avg `0.8274` n `12`; crypto_alt avg `1.4361` n `228`; crypto_major avg `2.766` n `8`; equity avg `1.416` n `74`; fx avg `-0.0947` n `6`; index avg `0.2209` n `23`; metal avg `0.4024` n `18`; unknown avg `-5.0099` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
