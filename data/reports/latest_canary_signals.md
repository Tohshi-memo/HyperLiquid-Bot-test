# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T14:07:44.625485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2034` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1008` n `13`; crypto_alt avg `-0.2135` n `239`; crypto_major avg `-0.1283` n `8`; equity avg `-0.0061` n `168`; fx avg `0.0214` n `6`; index avg `0.02` n `27`; metal avg `0.02` n `20`; unknown avg `0.5716` n `1253`
- 1h: commodity avg `-0.0499` n `13`; crypto_alt avg `-0.6821` n `239`; crypto_major avg `-1.0589` n `8`; equity avg `-0.7048` n `168`; fx avg `0.033` n `6`; index avg `-0.0613` n `27`; metal avg `-0.2709` n `20`; unknown avg `-0.0929` n `1255`
- 4h: commodity avg `0.0641` n `13`; crypto_alt avg `-1.5282` n `239`; crypto_major avg `-1.3509` n `8`; equity avg `-1.1683` n `168`; fx avg `0.0386` n `6`; index avg `-0.1475` n `27`; metal avg `-0.398` n `20`; unknown avg `244.4757` n `1185`
- 24h: commodity avg `0.1973` n `13`; crypto_alt avg `-2.7641` n `239`; crypto_major avg `-3.8263` n `8`; equity avg `-5.5507` n `168`; fx avg `-0.0225` n `6`; index avg `-0.4691` n `27`; metal avg `-1.215` n `20`; unknown avg `631.346` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
