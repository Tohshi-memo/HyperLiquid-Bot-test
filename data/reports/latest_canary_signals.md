# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T16:37:32.216356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0845` n `12`; crypto_alt avg `-0.4596` n `228`; crypto_major avg `-0.6376` n `8`; equity avg `-0.0251` n `74`; fx avg `0.0165` n `6`; index avg `0.0011` n `23`; metal avg `0.1005` n `18`; unknown avg `4.6564` n `548`
- 1h: commodity avg `0.5931` n `12`; crypto_alt avg `-0.351` n `228`; crypto_major avg `-0.5193` n `8`; equity avg `0.3199` n `74`; fx avg `-0.0003` n `6`; index avg `0.2431` n `23`; metal avg `0.2242` n `18`; unknown avg `0.2163` n `548`
- 4h: commodity avg `0.4554` n `12`; crypto_alt avg `0.3167` n `228`; crypto_major avg `0.365` n `8`; equity avg `0.2707` n `74`; fx avg `0.0064` n `6`; index avg `-0.1839` n `23`; metal avg `0.2009` n `18`; unknown avg `2.5081` n `547`
- 24h: commodity avg `2.1929` n `12`; crypto_alt avg `1.0787` n `228`; crypto_major avg `-0.0428` n `8`; equity avg `2.008` n `74`; fx avg `-0.0739` n `6`; index avg `0.9049` n `23`; metal avg `-0.9571` n `18`; unknown avg `-0.0117` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1117`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.09`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0662`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0591`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0586`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0558`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0495`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0475`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0468`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0457`, n `669`, weak_sample_signal
