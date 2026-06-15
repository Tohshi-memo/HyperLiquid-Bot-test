# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T05:07:31.423784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.79` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `-0.1823` n `228`; crypto_major avg `-0.1105` n `8`; equity avg `-0.0326` n `74`; fx avg `0.0157` n `6`; index avg `0.0823` n `23`; metal avg `-0.0448` n `18`; unknown avg `-0.0884` n `645`
- 1h: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.226` n `228`; crypto_major avg `-0.3057` n `8`; equity avg `0.0164` n `74`; fx avg `0.0197` n `6`; index avg `0.0465` n `23`; metal avg `0.0437` n `18`; unknown avg `-0.229` n `645`
- 4h: commodity avg `-0.1048` n `12`; crypto_alt avg `0.7208` n `228`; crypto_major avg `0.3956` n `8`; equity avg `0.3169` n `74`; fx avg `0.0514` n `6`; index avg `0.1804` n `23`; metal avg `0.4014` n `18`; unknown avg `-0.5879` n `629`
- 24h: commodity avg `-0.9033` n `12`; crypto_alt avg `2.7342` n `228`; crypto_major avg `2.6095` n `8`; equity avg `1.8403` n `74`; fx avg `0.041` n `6`; index avg `0.8958` n `23`; metal avg `2.0271` n `18`; unknown avg `3.1446` n `585`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
