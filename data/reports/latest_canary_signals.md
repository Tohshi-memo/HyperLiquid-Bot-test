# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T14:37:35.928895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9527` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.5532` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.522` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.233` n `12`; crypto_alt avg `0.7398` n `228`; crypto_major avg `1.1622` n `8`; equity avg `0.2143` n `74`; fx avg `0.009` n `6`; index avg `-0.0596` n `23`; metal avg `-0.0081` n `18`; unknown avg `0.0732` n `643`
- 1h: commodity avg `0.2655` n `12`; crypto_alt avg `0.6566` n `228`; crypto_major avg `1.1689` n `8`; equity avg `0.7401` n `74`; fx avg `-0.0071` n `6`; index avg `0.263` n `23`; metal avg `-0.3843` n `18`; unknown avg `16.5077` n `643`
- 4h: commodity avg `0.9282` n `12`; crypto_alt avg `0.0745` n `228`; crypto_major avg `1.176` n `8`; equity avg `-0.346` n `74`; fx avg `-0.0263` n `6`; index avg `0.1262` n `23`; metal avg `-0.7767` n `18`; unknown avg `15.9279` n `643`
- 24h: commodity avg `-1.5606` n `12`; crypto_alt avg `1.8689` n `228`; crypto_major avg `2.7946` n `8`; equity avg `2.3396` n `74`; fx avg `0.0663` n `6`; index avg `1.5783` n `23`; metal avg `2.1016` n `18`; unknown avg `23.0148` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
