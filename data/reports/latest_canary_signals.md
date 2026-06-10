# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T10:22:00.011364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1106` n `12`; crypto_alt avg `-0.0762` n `228`; crypto_major avg `0.0028` n `8`; equity avg `-0.0512` n `74`; fx avg `-0.0019` n `6`; index avg `-0.0153` n `23`; metal avg `0.1581` n `18`; unknown avg `0.0163` n `547`
- 1h: commodity avg `0.4692` n `12`; crypto_alt avg `0.3672` n `228`; crypto_major avg `0.3789` n `8`; equity avg `0.2787` n `74`; fx avg `0.0096` n `6`; index avg `0.1132` n `23`; metal avg `0.1768` n `18`; unknown avg `0.0584` n `547`
- 4h: commodity avg `0.8488` n `12`; crypto_alt avg `-0.2366` n `228`; crypto_major avg `-0.3562` n `8`; equity avg `-0.8453` n `74`; fx avg `-0.0007` n `6`; index avg `-0.3467` n `23`; metal avg `-0.6416` n `18`; unknown avg `0.1978` n `547`
- 24h: commodity avg `-0.2942` n `12`; crypto_alt avg `-1.326` n `228`; crypto_major avg `-3.624` n `8`; equity avg `-4.3166` n `74`; fx avg `0.0071` n `6`; index avg `-2.3557` n `23`; metal avg `-3.4635` n `18`; unknown avg `0.0375` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
