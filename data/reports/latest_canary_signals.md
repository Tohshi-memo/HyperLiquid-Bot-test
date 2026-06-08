# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T17:52:29.741188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0437` n `12`; crypto_alt avg `0.3653` n `228`; crypto_major avg `0.23` n `8`; equity avg `0.1341` n `74`; fx avg `0.0101` n `6`; index avg `0.1186` n `23`; metal avg `-0.0977` n `18`; unknown avg `-0.1586` n `517`
- 1h: commodity avg `-0.0693` n `12`; crypto_alt avg `0.3622` n `228`; crypto_major avg `0.0199` n `8`; equity avg `-0.2622` n `74`; fx avg `-0.0013` n `6`; index avg `-0.2073` n `23`; metal avg `-0.3234` n `18`; unknown avg `-0.1335` n `517`
- 4h: commodity avg `0.1132` n `12`; crypto_alt avg `0.4205` n `228`; crypto_major avg `0.1078` n `8`; equity avg `0.5278` n `74`; fx avg `-0.0104` n `6`; index avg `-0.0047` n `23`; metal avg `-0.0008` n `18`; unknown avg `-0.5191` n `517`
- 24h: commodity avg `-0.6076` n `12`; crypto_alt avg `2.4403` n `228`; crypto_major avg `2.8845` n `8`; equity avg `2.1923` n `74`; fx avg `-0.2841` n `6`; index avg `0.9748` n `23`; metal avg `-0.1701` n `18`; unknown avg `-1.8061` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
