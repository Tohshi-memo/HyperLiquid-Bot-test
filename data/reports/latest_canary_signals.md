# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T14:37:30.074100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.067` n `12`; crypto_alt avg `0.0054` n `229`; crypto_major avg `0.0325` n `8`; equity avg `0.3642` n `91`; fx avg `-0.0059` n `6`; index avg `0.0678` n `25`; metal avg `0.1025` n `20`; unknown avg `-0.0329` n `765`
- 1h: commodity avg `-0.2265` n `12`; crypto_alt avg `0.0455` n `229`; crypto_major avg `-0.0861` n `8`; equity avg `-0.2157` n `91`; fx avg `0.0021` n `6`; index avg `-0.0648` n `25`; metal avg `0.0692` n `20`; unknown avg `-0.0372` n `765`
- 4h: commodity avg `-0.5744` n `12`; crypto_alt avg `0.0601` n `229`; crypto_major avg `-0.2007` n `8`; equity avg `0.5725` n `91`; fx avg `-0.0252` n `6`; index avg `0.2021` n `25`; metal avg `0.3929` n `20`; unknown avg `0.12` n `764`
- 24h: commodity avg `-1.1123` n `12`; crypto_alt avg `1.2176` n `229`; crypto_major avg `0.6514` n `8`; equity avg `2.014` n `91`; fx avg `0.0713` n `6`; index avg `0.4062` n `25`; metal avg `1.0542` n `20`; unknown avg `0.9024` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
