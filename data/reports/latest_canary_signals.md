# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T17:52:19.506724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.854` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.7657` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `0.1847` n `228`; crypto_major avg `0.1395` n `8`; equity avg `0.0228` n `67`; fx avg `0.0032` n `6`; index avg `0.0514` n `23`; metal avg `0.0282` n `18`; unknown avg `-0.2353` n `418`
- 1h: commodity avg `-0.1739` n `12`; crypto_alt avg `-0.8915` n `228`; crypto_major avg `-0.6118` n `8`; equity avg `0.1338` n `67`; fx avg `0.0057` n `6`; index avg `0.0835` n `23`; metal avg `-0.0842` n `18`; unknown avg `-0.0584` n `418`
- 4h: commodity avg `-0.4468` n `12`; crypto_alt avg `-1.898` n `228`; crypto_major avg `-1.686` n `8`; equity avg `0.168` n `67`; fx avg `0.0206` n `6`; index avg `0.0797` n `23`; metal avg `-0.2747` n `18`; unknown avg `1.7879` n `416`
- 24h: commodity avg `1.0751` n `12`; crypto_alt avg `-2.3209` n `228`; crypto_major avg `-1.6761` n `8`; equity avg `-0.3497` n `67`; fx avg `-0.1078` n `6`; index avg `0.3809` n `23`; metal avg `-1.3486` n `18`; unknown avg `0.0295` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
