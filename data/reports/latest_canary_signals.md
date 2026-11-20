# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T05:22:27.400936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3917` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0249` n `13`; crypto_alt avg `0.0453` n `239`; crypto_major avg `0.0584` n `8`; equity avg `-0.1449` n `165`; fx avg `-0.0004` n `6`; index avg `-0.0073` n `27`; metal avg `-0.0302` n `20`; unknown avg `0.4009` n `1260`
- 1h: commodity avg `-0.031` n `13`; crypto_alt avg `-0.3631` n `239`; crypto_major avg `-0.4417` n `8`; equity avg `-0.6681` n `165`; fx avg `-0.021` n `6`; index avg `-0.0222` n `27`; metal avg `-0.1448` n `20`; unknown avg `159.9146` n `1250`
- 4h: commodity avg `-0.014` n `13`; crypto_alt avg `-1.9581` n `239`; crypto_major avg `-1.4986` n `8`; equity avg `-1.1635` n `165`; fx avg `-0.0025` n `6`; index avg `-0.1069` n `27`; metal avg `-0.4855` n `20`; unknown avg `164.742` n `1244`
- 24h: commodity avg `-0.0841` n `13`; crypto_alt avg `-3.4824` n `239`; crypto_major avg `-2.8135` n `8`; equity avg `-6.193` n `165`; fx avg `0.0058` n `6`; index avg `-0.5169` n `27`; metal avg `-1.8406` n `20`; unknown avg `222.0268` n `1167`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
