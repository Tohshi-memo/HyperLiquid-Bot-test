# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T16:52:19.203450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0868` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0622` n `12`; crypto_alt avg `-0.2883` n `228`; crypto_major avg `-0.3792` n `8`; equity avg `-0.1715` n `67`; fx avg `-0.0009` n `6`; index avg `-0.0875` n `23`; metal avg `-0.1173` n `18`; unknown avg `-0.1789` n `418`
- 1h: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.2279` n `228`; crypto_major avg `-0.1496` n `8`; equity avg `0.1541` n `67`; fx avg `0.0214` n `6`; index avg `0.1411` n `23`; metal avg `0.0057` n `18`; unknown avg `0.1976` n `418`
- 4h: commodity avg `0.4085` n `12`; crypto_alt avg `-0.966` n `228`; crypto_major avg `-0.748` n `8`; equity avg `-0.0611` n `67`; fx avg `-0.0089` n `6`; index avg `0.3388` n `23`; metal avg `-0.117` n `18`; unknown avg `1.0685` n `416`
- 24h: commodity avg `1.2812` n `12`; crypto_alt avg `-1.7863` n `228`; crypto_major avg `-1.4733` n `8`; equity avg `-0.4448` n `67`; fx avg `-0.1107` n `6`; index avg `0.3887` n `23`; metal avg `-1.321` n `18`; unknown avg `0.0315` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
