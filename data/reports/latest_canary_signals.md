# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T17:40:35.588582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0664` n `12`; crypto_alt avg `-0.03` n `228`; crypto_major avg `-0.0346` n `8`; equity avg `0.1172` n `67`; fx avg `-0.0014` n `6`; index avg `0.0089` n `23`; metal avg `0.0133` n `18`; unknown avg `0.0586` n `396`
- 1h: commodity avg `0.141` n `12`; crypto_alt avg `0.2828` n `228`; crypto_major avg `0.0355` n `8`; equity avg `0.0538` n `67`; fx avg `-0.0028` n `6`; index avg `0.0276` n `23`; metal avg `0.0423` n `18`; unknown avg `-0.0113` n `396`
- 4h: commodity avg `-0.6057` n `12`; crypto_alt avg `1.7711` n `228`; crypto_major avg `1.1786` n `8`; equity avg `0.6393` n `67`; fx avg `0.0069` n `6`; index avg `0.1639` n `23`; metal avg `0.2153` n `18`; unknown avg `0.8196` n `396`
- 24h: commodity avg `0.6464` n `12`; crypto_alt avg `-2.9766` n `228`; crypto_major avg `-2.1371` n `8`; equity avg `-1.0085` n `67`; fx avg `0.0158` n `6`; index avg `-0.3423` n `23`; metal avg `-0.2185` n `18`; unknown avg `-1.5635` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
