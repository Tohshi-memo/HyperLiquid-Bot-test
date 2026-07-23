# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T19:22:25.783773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `-0.0726` n `230`; crypto_major avg `-0.1178` n `8`; equity avg `0.0493` n `100`; fx avg `0.0049` n `6`; index avg `0.0285` n `25`; metal avg `0.0229` n `20`; unknown avg `0.0099` n `772`
- 1h: commodity avg `-0.1766` n `12`; crypto_alt avg `-0.001` n `230`; crypto_major avg `-0.0641` n `8`; equity avg `-0.2335` n `100`; fx avg `0.0051` n `6`; index avg `-0.0074` n `25`; metal avg `0.035` n `20`; unknown avg `-0.0808` n `772`
- 4h: commodity avg `-0.1738` n `12`; crypto_alt avg `-0.4344` n `230`; crypto_major avg `-0.4244` n `8`; equity avg `0.2934` n `100`; fx avg `0.0239` n `6`; index avg `0.0846` n `25`; metal avg `0.0087` n `20`; unknown avg `-0.4268` n `772`
- 24h: commodity avg `0.7903` n `12`; crypto_alt avg `-1.5811` n `230`; crypto_major avg `-2.2217` n `8`; equity avg `-1.5264` n `99`; fx avg `-0.0792` n `6`; index avg `-0.3483` n `25`; metal avg `-0.8027` n `20`; unknown avg `-0.3767` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
