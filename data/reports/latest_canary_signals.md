# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T23:08:52.419003+00:00`
- Correlation status: `ready`
- Asset price records: `115`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0354` n `7`; crypto_alt avg `-0.0702` n `223`; crypto_major avg `-0.0641` n `7`; equity avg `0.07` n `42`; fx avg `0.0027` n `4`; index avg `-0.0121` n `9`; metal avg `-0.0068` n `7`; unknown avg `-0.0628` n `313`
- 1h: commodity avg `0.0691` n `7`; crypto_alt avg `-0.2494` n `223`; crypto_major avg `-0.2331` n `7`; equity avg `-0.0468` n `42`; fx avg `-0.0109` n `4`; index avg `-0.0198` n `9`; metal avg `0.0024` n `7`; unknown avg `-0.0602` n `313`
- 4h: commodity avg `0.013` n `7`; crypto_alt avg `0.1719` n `223`; crypto_major avg `-0.0312` n `7`; equity avg `0.3651` n `42`; fx avg `0.0353` n `4`; index avg `-0.0128` n `9`; metal avg `-0.0018` n `7`; unknown avg `0.0669` n `313`
- 24h: commodity avg `-0.1506` n `7`; crypto_alt avg `1.9864` n `223`; crypto_major avg `0.7423` n `7`; equity avg `0.8027` n `42`; fx avg `0.012` n `4`; index avg `-0.0455` n `9`; metal avg `0.022` n `7`; unknown avg `0.3017` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4863`, n `111`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.4741`, n `107`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4694`, n `111`, moderate_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4259`, n `107`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4171`, n `107`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4168`, n `107`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4149`, n `107`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4132`, n `107`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4031`, n `111`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3852`, n `111`, moderate_sample_signal
