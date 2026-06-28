# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T20:52:32.921463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0191` n `12`; crypto_alt avg `-0.1516` n `228`; crypto_major avg `-0.0724` n `8`; equity avg `0.0421` n `88`; fx avg `0.0008` n `6`; index avg `0.0087` n `23`; metal avg `0.0146` n `20`; unknown avg `-0.2045` n `764`
- 1h: commodity avg `-0.32` n `12`; crypto_alt avg `0.3316` n `228`; crypto_major avg `0.3932` n `8`; equity avg `0.2209` n `88`; fx avg `-0.0263` n `6`; index avg `0.0673` n `23`; metal avg `0.0542` n `20`; unknown avg `3.8528` n `764`
- 4h: commodity avg `-0.3871` n `12`; crypto_alt avg `-0.3888` n `228`; crypto_major avg `-0.196` n `8`; equity avg `0.1189` n `88`; fx avg `-0.0726` n `6`; index avg `0.0549` n `23`; metal avg `0.0564` n `20`; unknown avg `4.4343` n `764`
- 24h: commodity avg `0.0288` n `12`; crypto_alt avg `-0.4343` n `228`; crypto_major avg `-0.9422` n `8`; equity avg `0.2562` n `88`; fx avg `-0.073` n `6`; index avg `-0.0001` n `23`; metal avg `0.0342` n `20`; unknown avg `16.1274` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
