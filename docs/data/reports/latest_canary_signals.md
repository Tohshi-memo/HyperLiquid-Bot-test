# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T22:52:17.176923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.269` n `12`; crypto_alt avg `0.0137` n `228`; crypto_major avg `0.0505` n `8`; equity avg `0.0416` n `67`; fx avg `0.0043` n `6`; index avg `-0.007` n `23`; metal avg `0.1624` n `18`; unknown avg `0.0039` n `396`
- 1h: commodity avg `-0.9782` n `12`; crypto_alt avg `0.8768` n `228`; crypto_major avg `0.7356` n `8`; equity avg `0.0909` n `67`; fx avg `0.0281` n `6`; index avg `0.0467` n `23`; metal avg `1.4417` n `18`; unknown avg `0.5582` n `396`
- 4h: commodity avg `-0.9138` n `12`; crypto_alt avg `-0.5844` n `228`; crypto_major avg `-0.2997` n `8`; equity avg `-0.0157` n `67`; fx avg `0.0808` n `6`; index avg `-0.0173` n `23`; metal avg `0.9815` n `18`; unknown avg `-0.2876` n `396`
- 24h: commodity avg `0.5407` n `12`; crypto_alt avg `-1.8034` n `228`; crypto_major avg `0.48` n `8`; equity avg `0.3532` n `67`; fx avg `0.0931` n `6`; index avg `0.1429` n `23`; metal avg `0.9545` n `18`; unknown avg `0.2375` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
