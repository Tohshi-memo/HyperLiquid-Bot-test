# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T07:58:06.871353+00:00`
- Correlation status: `ready`
- Asset price records: `54`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0452` n `7`; crypto_alt avg `-0.0282` n `223`; crypto_major avg `-0.0272` n `7`; equity avg `-0.0288` n `42`; fx avg `0.0128` n `4`; index avg `0.0138` n `9`; metal avg `0.0133` n `7`; unknown avg `0.1927` n `311`
- 1h: commodity avg `0.0113` n `7`; crypto_alt avg `0.1985` n `223`; crypto_major avg `0.1332` n `7`; equity avg `0.0357` n `42`; fx avg `0.0192` n `4`; index avg `-0.008` n `9`; metal avg `0.0245` n `7`; unknown avg `0.1465` n `311`
- 4h: commodity avg `0.0196` n `7`; crypto_alt avg `0.0052` n `223`; crypto_major avg `-0.0089` n `7`; equity avg `0.0742` n `42`; fx avg `-0.1217` n `4`; index avg `-0.0376` n `9`; metal avg `0.0375` n `7`; unknown avg `0.2431` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6039`, n `50`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5828`, n `50`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5821`, n `46`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5562`, n `50`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5422`, n `46`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5221`, n `50`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4832`, n `50`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4607`, n `46`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4427`, n `46`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4423`, n `46`, moderate_sample_signal
