# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T09:07:27.391013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1331` n `12`; crypto_alt avg `-0.4142` n `228`; crypto_major avg `-0.3127` n `8`; equity avg `-0.0712` n `74`; fx avg `-0.0005` n `6`; index avg `0.0268` n `23`; metal avg `-0.0096` n `18`; unknown avg `-0.1005` n `547`
- 1h: commodity avg `-0.506` n `12`; crypto_alt avg `0.0259` n `228`; crypto_major avg `0.1533` n `8`; equity avg `0.1902` n `74`; fx avg `0.0333` n `6`; index avg `0.2402` n `23`; metal avg `0.2067` n `18`; unknown avg `-0.1527` n `547`
- 4h: commodity avg `-0.2886` n `12`; crypto_alt avg `-0.0151` n `228`; crypto_major avg `-0.0868` n `8`; equity avg `0.0926` n `74`; fx avg `0.0907` n `6`; index avg `0.2426` n `23`; metal avg `0.2946` n `18`; unknown avg `0.2984` n `503`
- 24h: commodity avg `-1.4302` n `12`; crypto_alt avg `0.2722` n `228`; crypto_major avg `0.8245` n `8`; equity avg `2.2886` n `74`; fx avg `0.0353` n `6`; index avg `1.3014` n `23`; metal avg `0.9681` n `18`; unknown avg `-2.8104` n `503`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
