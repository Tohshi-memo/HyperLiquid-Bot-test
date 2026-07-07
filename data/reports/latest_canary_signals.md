# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T05:52:28.281581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0354` n `12`; crypto_alt avg `0.1347` n `229`; crypto_major avg `0.1363` n `8`; equity avg `0.25` n `91`; fx avg `-0.0024` n `6`; index avg `0.0567` n `25`; metal avg `-0.021` n `20`; unknown avg `17.6242` n `763`
- 1h: commodity avg `0.0878` n `12`; crypto_alt avg `0.2645` n `229`; crypto_major avg `0.3369` n `8`; equity avg `0.5672` n `91`; fx avg `0.0101` n `6`; index avg `0.0901` n `25`; metal avg `-0.158` n `20`; unknown avg `7.2118` n `763`
- 4h: commodity avg `0.0158` n `12`; crypto_alt avg `-0.9091` n `229`; crypto_major avg `-1.0922` n `8`; equity avg `-0.6502` n `91`; fx avg `-0.0365` n `6`; index avg `-0.1926` n `25`; metal avg `-0.4239` n `20`; unknown avg `21.0319` n `763`
- 24h: commodity avg `0.2131` n `12`; crypto_alt avg `0.466` n `229`; crypto_major avg `-0.4572` n `8`; equity avg `-1.3155` n `90`; fx avg `-0.0157` n `6`; index avg `-0.29` n `25`; metal avg `-0.4808` n `20`; unknown avg `-0.4273` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
