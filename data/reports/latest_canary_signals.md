# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T03:07:24.476923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.147` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.032` n `13`; crypto_alt avg `0.0628` n `239`; crypto_major avg `0.117` n `8`; equity avg `0.0783` n `168`; fx avg `-0.0093` n `6`; index avg `0.0239` n `27`; metal avg `-0.0204` n `20`; unknown avg `-0.0399` n `1255`
- 1h: commodity avg `-0.1086` n `13`; crypto_alt avg `0.1107` n `239`; crypto_major avg `0.2578` n `8`; equity avg `-0.5389` n `168`; fx avg `-0.0236` n `6`; index avg `-0.0199` n `27`; metal avg `-0.145` n `20`; unknown avg `0.0861` n `1259`
- 4h: commodity avg `-0.2083` n `13`; crypto_alt avg `-0.6712` n `239`; crypto_major avg `-1.3426` n `8`; equity avg `-2.0336` n `168`; fx avg `-0.0056` n `6`; index avg `-0.1956` n `27`; metal avg `-0.1384` n `20`; unknown avg `331.7196` n `1219`
- 24h: commodity avg `0.3776` n `13`; crypto_alt avg `-2.1378` n `239`; crypto_major avg `-1.7024` n `8`; equity avg `-4.754` n `167`; fx avg `0.1766` n `6`; index avg `-0.4716` n `27`; metal avg `-0.9755` n `20`; unknown avg `442.3858` n `1029`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
