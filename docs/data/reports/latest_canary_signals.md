# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T19:09:00.210953+00:00`
- Correlation status: `ready`
- Asset price records: `576`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.0636` n `228`; crypto_major avg `0.0094` n `8`; equity avg `0.0376` n `65`; fx avg `-0.0153` n `5`; index avg `0.1169` n `23`; metal avg `0.2313` n `18`; unknown avg `-0.243` n `365`
- 1h: commodity avg `0.4609` n `12`; crypto_alt avg `-0.2303` n `228`; crypto_major avg `-0.3637` n `8`; equity avg `-0.458` n `65`; fx avg `0.0063` n `5`; index avg `-0.2723` n `23`; metal avg `-0.3275` n `18`; unknown avg `-0.1891` n `365`
- 4h: commodity avg `1.4788` n `12`; crypto_alt avg `0.7461` n `228`; crypto_major avg `-0.3032` n `8`; equity avg `-1.5019` n `65`; fx avg `0.0425` n `5`; index avg `-0.9126` n `23`; metal avg `-1.5854` n `18`; unknown avg `-0.1945` n `365`
- 24h: commodity avg `0.6532` n `12`; crypto_alt avg `1.0538` n `228`; crypto_major avg `-1.9066` n `8`; equity avg `-1.2043` n `65`; fx avg `0.1803` n `5`; index avg `-0.8221` n `23`; metal avg `0.2629` n `18`; unknown avg `-0.1234` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1392`, n `572`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1169`, n `572`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1057`, n `572`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `572`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `568`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `568`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0923`, n `568`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0877`, n `568`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0873`, n `568`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0838`, n `568`, weak_sample_signal
