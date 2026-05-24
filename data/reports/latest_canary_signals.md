# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T11:37:14.897173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.025` n `12`; crypto_alt avg `0.015` n `228`; crypto_major avg `0.1079` n `8`; equity avg `0.0898` n `67`; fx avg `-0.0139` n `6`; index avg `0.0412` n `23`; metal avg `0.0163` n `18`; unknown avg `0.0573` n `396`
- 1h: commodity avg `0.0232` n `12`; crypto_alt avg `-0.0276` n `228`; crypto_major avg `0.2854` n `8`; equity avg `0.0319` n `67`; fx avg `0.0008` n `6`; index avg `-0.0201` n `23`; metal avg `-0.0013` n `18`; unknown avg `0.331` n `396`
- 4h: commodity avg `0.1452` n `12`; crypto_alt avg `-0.0116` n `228`; crypto_major avg `0.73` n `8`; equity avg `0.2314` n `67`; fx avg `0.0013` n `6`; index avg `-0.0808` n `23`; metal avg `0.0743` n `18`; unknown avg `-0.2564` n `396`
- 24h: commodity avg `-2.6077` n `12`; crypto_alt avg `3.7766` n `228`; crypto_major avg `4.7804` n `8`; equity avg `2.7281` n `67`; fx avg `0.0557` n `6`; index avg `1.3178` n `23`; metal avg `1.3448` n `18`; unknown avg `1.4847` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
