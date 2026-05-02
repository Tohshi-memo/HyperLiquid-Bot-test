# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T12:15:17.624199+00:00`
- Correlation status: `ready`
- Asset price records: `72`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `7`; crypto_alt avg `0.0645` n `223`; crypto_major avg `-0.0178` n `7`; equity avg `-0.0292` n `42`; fx avg `-0.0013` n `4`; index avg `0.0` n `9`; metal avg `0.0061` n `7`; unknown avg `0.0047` n `313`
- 1h: commodity avg `-0.075` n `7`; crypto_alt avg `0.0912` n `223`; crypto_major avg `-0.0856` n `7`; equity avg `0.013` n `42`; fx avg `0.0107` n `4`; index avg `0.014` n `9`; metal avg `0.0038` n `7`; unknown avg `-0.1145` n `313`
- 4h: commodity avg `-0.0502` n `7`; crypto_alt avg `0.2856` n `223`; crypto_major avg `-0.1487` n `7`; equity avg `-0.0878` n `42`; fx avg `-0.0064` n `4`; index avg `0.0066` n `9`; metal avg `0.0398` n `7`; unknown avg `-0.1291` n `313`
- 24h: crypto_alt avg `0.8194` n `223`; crypto_major avg `0.523` n `7`; metal avg `0.7906` n `1`; unknown avg `1.2979` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5741`, n `68`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5543`, n `68`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.549`, n `64`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5391`, n `64`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4946`, n `68`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4762`, n `64`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4718`, n `64`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4631`, n `64`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4594`, n `68`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.455`, n `68`, moderate_sample_signal
