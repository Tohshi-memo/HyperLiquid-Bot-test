# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T12:07:30.235453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `13`; crypto_alt avg `-0.2625` n `236`; crypto_major avg `-0.1511` n `8`; equity avg `-0.0686` n `151`; fx avg `0.0004` n `6`; index avg `-0.0258` n `26`; metal avg `-0.0094` n `20`; unknown avg `0.03` n `1185`
- 1h: commodity avg `0.0107` n `13`; crypto_alt avg `-0.4296` n `236`; crypto_major avg `-0.3583` n `8`; equity avg `-0.151` n `151`; fx avg `-0.0005` n `6`; index avg `-0.021` n `26`; metal avg `-0.0049` n `20`; unknown avg `-0.1848` n `1185`
- 4h: commodity avg `0.0784` n `13`; crypto_alt avg `-0.6384` n `236`; crypto_major avg `-0.479` n `8`; equity avg `-0.0386` n `151`; fx avg `0.0066` n `6`; index avg `-0.0151` n `26`; metal avg `0.0067` n `20`; unknown avg `0.196` n `1183`
- 24h: commodity avg `0.3098` n `13`; crypto_alt avg `-2.8204` n `236`; crypto_major avg `-1.825` n `8`; equity avg `-3.4533` n `151`; fx avg `0.0085` n `6`; index avg `-0.5731` n `26`; metal avg `-0.2172` n `20`; unknown avg `8.8947` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1845`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1488`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
