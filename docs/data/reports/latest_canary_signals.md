# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T04:37:23.415958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `-0.0734` n `230`; crypto_major avg `-0.0325` n `8`; equity avg `-0.1083` n `120`; fx avg `-0.0017` n `6`; index avg `-0.0135` n `25`; metal avg `-0.0241` n `20`; unknown avg `0.1865` n `789`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `-0.1272` n `230`; crypto_major avg `0.0673` n `8`; equity avg `-0.3133` n `120`; fx avg `-0.003` n `6`; index avg `-0.0524` n `25`; metal avg `-0.0779` n `20`; unknown avg `0.6242` n `789`
- 4h: commodity avg `-0.035` n `12`; crypto_alt avg `0.0858` n `230`; crypto_major avg `-0.1147` n `8`; equity avg `0.0736` n `120`; fx avg `-0.1038` n `6`; index avg `-0.0363` n `25`; metal avg `-0.0155` n `20`; unknown avg `0.2968` n `789`
- 24h: commodity avg `0.2981` n `12`; crypto_alt avg `0.4083` n `230`; crypto_major avg `0.2142` n `8`; equity avg `-3.4049` n `120`; fx avg `-0.1678` n `6`; index avg `-0.5491` n `25`; metal avg `-0.557` n `20`; unknown avg `-0.2201` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
