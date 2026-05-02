# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T15:30:22.769105+00:00`
- Correlation status: `ready`
- Asset price records: `85`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `7`; crypto_alt avg `0.0087` n `223`; crypto_major avg `-0.0036` n `7`; equity avg `-0.039` n `42`; fx avg `0.0` n `4`; index avg `-0.0028` n `9`; metal avg `-0.0018` n `7`; unknown avg `-0.0174` n `313`
- 1h: commodity avg `-0.0178` n `7`; crypto_alt avg `0.3163` n `223`; crypto_major avg `0.0657` n `7`; equity avg `-0.0222` n `42`; fx avg `0.0349` n `4`; index avg `-0.0054` n `9`; metal avg `0.004` n `7`; unknown avg `-0.1427` n `313`
- 4h: commodity avg `-0.0398` n `7`; crypto_alt avg `1.137` n `223`; crypto_major avg `0.2398` n `7`; equity avg `-0.0564` n `42`; fx avg `0.036` n `4`; index avg `0.024` n `9`; metal avg `-0.0066` n `7`; unknown avg `-0.0641` n `313`
- 24h: commodity avg `0.2758` n `7`; crypto_alt avg `1.1426` n `223`; crypto_major avg `-0.1215` n `7`; equity avg `0.5164` n `42`; fx avg `-0.1128` n `4`; index avg `0.0677` n `9`; metal avg `-0.332` n `7`; unknown avg `0.8548` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5415`, n `77`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5363`, n `77`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5342`, n `81`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5157`, n `81`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4783`, n `77`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4763`, n `77`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4656`, n `77`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4526`, n `81`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4311`, n `81`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4257`, n `77`, moderate_sample_signal
