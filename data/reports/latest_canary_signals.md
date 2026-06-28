# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T00:37:32.921532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0331` n `12`; crypto_alt avg `-0.0007` n `228`; crypto_major avg `-0.0693` n `8`; equity avg `0.0132` n `88`; fx avg `-0.0063` n `6`; index avg `-0.0001` n `23`; metal avg `-0.0055` n `20`; unknown avg `-0.1774` n `764`
- 1h: commodity avg `0.0921` n `12`; crypto_alt avg `0.2937` n `228`; crypto_major avg `0.1056` n `8`; equity avg `0.0646` n `88`; fx avg `-0.0259` n `6`; index avg `0.0087` n `23`; metal avg `0.0366` n `20`; unknown avg `6.1793` n `764`
- 4h: commodity avg `0.1909` n `12`; crypto_alt avg `-0.224` n `228`; crypto_major avg `-0.4516` n `8`; equity avg `-0.0177` n `88`; fx avg `-0.0148` n `6`; index avg `-0.0633` n `23`; metal avg `0.0313` n `20`; unknown avg `-0.4807` n `764`
- 24h: commodity avg `0.2194` n `12`; crypto_alt avg `-0.3703` n `228`; crypto_major avg `-0.6914` n `8`; equity avg `0.3354` n `88`; fx avg `0.0118` n `6`; index avg `-0.0642` n `23`; metal avg `-0.0294` n `20`; unknown avg `-0.7257` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
