# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T06:07:29.014067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.2088` n `228`; crypto_major avg `0.2799` n `8`; equity avg `0.023` n `78`; fx avg `-0.0041` n `6`; index avg `-0.0299` n `23`; metal avg `-0.0109` n `18`; unknown avg `-0.0222` n `655`
- 1h: commodity avg `0.0574` n `12`; crypto_alt avg `0.123` n `228`; crypto_major avg `0.4187` n `8`; equity avg `0.1299` n `78`; fx avg `-0.0053` n `6`; index avg `0.016` n `23`; metal avg `-0.0128` n `18`; unknown avg `7.2367` n `655`
- 4h: commodity avg `0.0528` n `12`; crypto_alt avg `0.539` n `228`; crypto_major avg `1.0972` n `8`; equity avg `0.4908` n `78`; fx avg `-0.0279` n `6`; index avg `0.034` n `23`; metal avg `-0.001` n `18`; unknown avg `0.098` n `655`
- 24h: commodity avg `0.4818` n `12`; crypto_alt avg `-3.082` n `228`; crypto_major avg `-3.3587` n `8`; equity avg `1.349` n `78`; fx avg `-0.1121` n `6`; index avg `0.3135` n `23`; metal avg `-4.1265` n `18`; unknown avg `-0.4941` n `546`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
