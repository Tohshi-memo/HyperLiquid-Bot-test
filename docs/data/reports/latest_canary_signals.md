# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T05:07:28.193681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `-0.0244` n `228`; crypto_major avg `-0.1372` n `8`; equity avg `0.0294` n `78`; fx avg `0.003` n `6`; index avg `0.0157` n `23`; metal avg `-0.0059` n `18`; unknown avg `0.1283` n `694`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.1511` n `228`; crypto_major avg `-0.2727` n `8`; equity avg `0.0295` n `78`; fx avg `0.1024` n `6`; index avg `0.0084` n `23`; metal avg `-0.0049` n `18`; unknown avg `-0.0547` n `694`
- 4h: commodity avg `0.0082` n `12`; crypto_alt avg `-0.0617` n `228`; crypto_major avg `-0.2733` n `8`; equity avg `0.1688` n `78`; fx avg `-0.0078` n `6`; index avg `0.0141` n `23`; metal avg `0.0337` n `18`; unknown avg `-0.2398` n `693`
- 24h: commodity avg `0.2175` n `12`; crypto_alt avg `0.8911` n `228`; crypto_major avg `0.5161` n `8`; equity avg `0.2926` n `78`; fx avg `0.0643` n `6`; index avg `0.0178` n `23`; metal avg `-0.0358` n `18`; unknown avg `-0.8667` n `549`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
