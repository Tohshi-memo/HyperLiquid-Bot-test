# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T09:07:18.975323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0281` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0421` n `12`; crypto_alt avg `0.0663` n `228`; crypto_major avg `0.0463` n `8`; equity avg `0.0106` n `67`; fx avg `0.0065` n `6`; index avg `-0.0059` n `23`; metal avg `-0.019` n `18`; unknown avg `0.2604` n `396`
- 1h: commodity avg `0.0264` n `12`; crypto_alt avg `0.654` n `228`; crypto_major avg `0.3306` n `8`; equity avg `0.1944` n `67`; fx avg `-0.0091` n `6`; index avg `0.011` n `23`; metal avg `0.0326` n `18`; unknown avg `0.2037` n `386`
- 4h: commodity avg `-0.1398` n `12`; crypto_alt avg `-1.894` n `228`; crypto_major avg `-1.1585` n `8`; equity avg `-0.2495` n `67`; fx avg `-0.0192` n `6`; index avg `-0.1304` n `23`; metal avg `-0.0021` n `18`; unknown avg `0.7492` n `376`
- 24h: commodity avg `-0.5868` n `12`; crypto_alt avg `-5.7315` n `228`; crypto_major avg `-3.9931` n `8`; equity avg `-1.7107` n `67`; fx avg `0.012` n `6`; index avg `-0.2364` n `23`; metal avg `-0.3816` n `18`; unknown avg `-1.2277` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
