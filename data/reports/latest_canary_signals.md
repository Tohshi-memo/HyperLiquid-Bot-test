# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T10:52:25.642361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `0.0351` n `228`; crypto_major avg `-0.0388` n `8`; equity avg `0.0291` n `88`; fx avg `0.0208` n `6`; index avg `-0.0028` n `23`; metal avg `-0.007` n `20`; unknown avg `0.0334` n `764`
- 1h: commodity avg `0.0155` n `12`; crypto_alt avg `0.0981` n `228`; crypto_major avg `0.13` n `8`; equity avg `0.0549` n `88`; fx avg `0.0201` n `6`; index avg `0.0048` n `23`; metal avg `-0.0034` n `20`; unknown avg `-0.0234` n `764`
- 4h: commodity avg `0.0696` n `12`; crypto_alt avg `-0.1938` n `228`; crypto_major avg `-0.1692` n `8`; equity avg `0.1007` n `88`; fx avg `0.019` n `6`; index avg `-0.013` n `23`; metal avg `-0.051` n `20`; unknown avg `-0.2161` n `748`
- 24h: commodity avg `0.1232` n `12`; crypto_alt avg `2.0503` n `228`; crypto_major avg `1.9461` n `8`; equity avg `1.9762` n `87`; fx avg `0.0364` n `6`; index avg `0.0819` n `23`; metal avg `0.3448` n `20`; unknown avg `0.0884` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
