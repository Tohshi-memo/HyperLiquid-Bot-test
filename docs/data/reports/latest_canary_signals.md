# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T17:37:23.279973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5556` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4036` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0465` n `12`; crypto_alt avg `-0.4536` n `228`; crypto_major avg `-0.3238` n `8`; equity avg `-0.0043` n `67`; fx avg `-0.0061` n `6`; index avg `-0.0043` n `23`; metal avg `-0.172` n `18`; unknown avg `0.8876` n `418`
- 1h: commodity avg `-0.1103` n `12`; crypto_alt avg `-1.1018` n `228`; crypto_major avg `-0.9906` n `8`; equity avg `-0.0569` n `67`; fx avg `0.0053` n `6`; index avg `-0.0582` n `23`; metal avg `-0.2328` n `18`; unknown avg `0.9923` n `418`
- 4h: commodity avg `-0.0575` n `12`; crypto_alt avg `-1.5642` n `228`; crypto_major avg `-1.2478` n `8`; equity avg `0.3078` n `67`; fx avg `-0.0025` n `6`; index avg `0.1558` n `23`; metal avg `-0.5757` n `18`; unknown avg `2.2243` n `416`
- 24h: commodity avg `1.2611` n `12`; crypto_alt avg `-2.573` n `228`; crypto_major avg `-1.8123` n `8`; equity avg `-0.351` n `67`; fx avg `-0.1073` n `6`; index avg `0.3148` n `23`; metal avg `-1.4497` n `18`; unknown avg `0.2448` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
