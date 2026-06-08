# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T11:22:21.911196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.6993` n `12`; crypto_alt avg `0.6813` n `228`; crypto_major avg `0.8369` n `8`; equity avg `0.6852` n `74`; fx avg `0.0086` n `6`; index avg `0.3795` n `23`; metal avg `0.8364` n `18`; unknown avg `0.1781` n `517`
- 1h: commodity avg `-1.0199` n `12`; crypto_alt avg `1.178` n `228`; crypto_major avg `0.8454` n `8`; equity avg `0.9014` n `74`; fx avg `0.0396` n `6`; index avg `0.4472` n `23`; metal avg `0.9778` n `18`; unknown avg `0.3197` n `517`
- 4h: commodity avg `-1.1194` n `12`; crypto_alt avg `1.4324` n `228`; crypto_major avg `0.6233` n `8`; equity avg `1.1188` n `74`; fx avg `0.0163` n `6`; index avg `0.6146` n `23`; metal avg `0.7017` n `18`; unknown avg `0.0004` n `517`
- 24h: commodity avg `-0.257` n `12`; crypto_alt avg `1.8586` n `228`; crypto_major avg `2.5674` n `8`; equity avg `1.8467` n `74`; fx avg `-0.2536` n `6`; index avg `0.9411` n `23`; metal avg `0.1285` n `18`; unknown avg `-2.2782` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
