# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T19:22:34.898975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0386` n `12`; crypto_alt avg `-0.0473` n `228`; crypto_major avg `0.0359` n `8`; equity avg `0.0026` n `78`; fx avg `-0.0013` n `6`; index avg `0.0018` n `23`; metal avg `0.0146` n `18`; unknown avg `0.0021` n `694`
- 1h: commodity avg `0.0931` n `12`; crypto_alt avg `0.2589` n `228`; crypto_major avg `0.3111` n `8`; equity avg `0.0349` n `78`; fx avg `-0.0049` n `6`; index avg `0.0167` n `23`; metal avg `0.0191` n `18`; unknown avg `0.3394` n `694`
- 4h: commodity avg `0.2576` n `12`; crypto_alt avg `0.034` n `228`; crypto_major avg `0.0205` n `8`; equity avg `-0.0381` n `78`; fx avg `-0.0952` n `6`; index avg `-0.0268` n `23`; metal avg `-0.0711` n `18`; unknown avg `-0.1916` n `694`
- 24h: commodity avg `0.3152` n `12`; crypto_alt avg `1.7065` n `228`; crypto_major avg `0.4929` n `8`; equity avg `0.3787` n `78`; fx avg `-0.0709` n `6`; index avg `0.0132` n `23`; metal avg `-0.0987` n `18`; unknown avg `0.1747` n `645`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
