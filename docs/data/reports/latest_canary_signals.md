# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T10:22:27.826163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0996` n `13`; crypto_alt avg `-0.043` n `239`; crypto_major avg `-0.0491` n `8`; equity avg `-0.0473` n `157`; fx avg `0.0063` n `6`; index avg `-0.0055` n `27`; metal avg `-0.0135` n `20`; unknown avg `-0.1724` n `1264`
- 1h: commodity avg `-0.0752` n `13`; crypto_alt avg `0.0236` n `239`; crypto_major avg `0.1192` n `8`; equity avg `0.2715` n `157`; fx avg `0.0046` n `6`; index avg `0.0288` n `27`; metal avg `0.0525` n `20`; unknown avg `6.948` n `1258`
- 4h: commodity avg `0.2419` n `13`; crypto_alt avg `0.5106` n `239`; crypto_major avg `0.6094` n `8`; equity avg `1.2783` n `157`; fx avg `0.0629` n `6`; index avg `0.1269` n `27`; metal avg `-0.155` n `20`; unknown avg `0.8124` n `1224`
- 24h: commodity avg `-0.4221` n `13`; crypto_alt avg `-1.6793` n `238`; crypto_major avg `-1.0041` n `8`; equity avg `-3.5279` n `157`; fx avg `0.0068` n `6`; index avg `-0.2254` n `27`; metal avg `-0.4435` n `20`; unknown avg `4.0361` n `1023`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
