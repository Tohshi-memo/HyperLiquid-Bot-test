# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T00:14:48.012967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.067` n `12`; crypto_alt avg `-0.2135` n `228`; crypto_major avg `-0.0954` n `8`; equity avg `-0.2259` n `74`; fx avg `0.0219` n `6`; index avg `-0.1285` n `23`; metal avg `0.0226` n `18`; unknown avg `-0.1407` n `517`
- 1h: commodity avg `-0.0779` n `12`; crypto_alt avg `-0.9431` n `228`; crypto_major avg `-0.7264` n `8`; equity avg `-0.2296` n `74`; fx avg `0.0299` n `6`; index avg `-0.1521` n `23`; metal avg `-0.239` n `18`; unknown avg `0.2781` n `517`
- 4h: commodity avg `-0.04` n `12`; crypto_alt avg `-1.3105` n `228`; crypto_major avg `-0.5918` n `8`; equity avg `-0.3094` n `74`; fx avg `0.0185` n `6`; index avg `-0.0622` n `23`; metal avg `-0.1823` n `18`; unknown avg `-0.9373` n `517`
- 24h: commodity avg `-0.6777` n `12`; crypto_alt avg `0.1767` n `228`; crypto_major avg `0.9444` n `8`; equity avg `1.5235` n `74`; fx avg `-0.2385` n `6`; index avg `0.6424` n `23`; metal avg `-0.5048` n `18`; unknown avg `-3.1403` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
