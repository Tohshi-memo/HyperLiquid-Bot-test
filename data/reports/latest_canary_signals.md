# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T11:37:27.085229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5679` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0423` n `13`; crypto_alt avg `-0.1095` n `238`; crypto_major avg `-0.0845` n `8`; equity avg `-0.1735` n `155`; fx avg `-0.0073` n `6`; index avg `-0.0409` n `27`; metal avg `-0.06` n `20`; unknown avg `-0.1398` n `1239`
- 1h: commodity avg `-0.0026` n `13`; crypto_alt avg `0.2281` n `238`; crypto_major avg `0.6675` n `8`; equity avg `0.0708` n `155`; fx avg `0.0031` n `6`; index avg `-0.0109` n `27`; metal avg `-0.0379` n `20`; unknown avg `2.301` n `1232`
- 4h: commodity avg `-0.1174` n `13`; crypto_alt avg `1.262` n `238`; crypto_major avg `1.4647` n `8`; equity avg `0.4122` n `155`; fx avg `0.0379` n `6`; index avg `0.043` n `27`; metal avg `-0.1032` n `20`; unknown avg `3.3345` n `1120`
- 24h: commodity avg `-0.3071` n `13`; crypto_alt avg `-2.0733` n `238`; crypto_major avg `-0.9236` n `8`; equity avg `-1.4553` n `155`; fx avg `0.0517` n `6`; index avg `-0.056` n `27`; metal avg `-0.468` n `20`; unknown avg `13.3843` n `982`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
