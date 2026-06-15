# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T16:52:38.414985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.19` - Polymarket crypto volume is unusually high.
- 1h_crypto_equity_divergence: score `-3.0017` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.1543` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0526` n `12`; crypto_alt avg `-0.1563` n `228`; crypto_major avg `0.0247` n `8`; equity avg `-0.1277` n `77`; fx avg `-0.0157` n `6`; index avg `-0.0557` n `23`; metal avg `-0.0478` n `18`; unknown avg `0.3769` n `687`
- 1h: commodity avg `0.2528` n `12`; crypto_alt avg `-0.3391` n `228`; crypto_major avg `0.1277` n `8`; equity avg `3.1294` n `77`; fx avg `0.0009` n `6`; index avg `-0.006` n `23`; metal avg `-0.4457` n `18`; unknown avg `0.1084` n `687`
- 4h: commodity avg `0.5276` n `12`; crypto_alt avg `0.6091` n `228`; crypto_major avg `1.6503` n `8`; equity avg `1.2857` n `76`; fx avg `-0.0064` n `6`; index avg `0.4457` n `23`; metal avg `-0.504` n `18`; unknown avg `1.037` n `687`
- 24h: commodity avg `-0.6871` n `12`; crypto_alt avg `6.3418` n `228`; crypto_major avg `7.8592` n `8`; equity avg `3.0011` n `76`; fx avg `0.0442` n `6`; index avg `1.3267` n `23`; metal avg `2.3289` n `18`; unknown avg `2.9365` n `527`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.151`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1357`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1143`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0936`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0931`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0672`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0653`, n `669`, weak_sample_signal
