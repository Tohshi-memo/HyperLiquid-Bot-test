# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T05:52:15.965072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0344` n `12`; crypto_alt avg `0.0889` n `228`; crypto_major avg `0.0504` n `8`; equity avg `-0.0033` n `67`; fx avg `0.0195` n `6`; index avg `0.0008` n `23`; metal avg `-0.166` n `18`; unknown avg `-0.0284` n `397`
- 1h: commodity avg `0.0268` n `12`; crypto_alt avg `0.2703` n `228`; crypto_major avg `0.0276` n `8`; equity avg `0.0615` n `67`; fx avg `0.0288` n `6`; index avg `-0.0094` n `23`; metal avg `-0.3196` n `18`; unknown avg `-0.6938` n `397`
- 4h: commodity avg `-0.5784` n `12`; crypto_alt avg `1.0376` n `228`; crypto_major avg `0.5864` n `8`; equity avg `0.3782` n `67`; fx avg `-0.004` n `6`; index avg `0.0996` n `23`; metal avg `-0.3005` n `18`; unknown avg `-0.5946` n `396`
- 24h: commodity avg `0.0155` n `12`; crypto_alt avg `0.3027` n `228`; crypto_major avg `0.2823` n `8`; equity avg `0.4924` n `67`; fx avg `-0.0398` n `6`; index avg `-0.1507` n `23`; metal avg `0.2496` n `18`; unknown avg `-0.107` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
