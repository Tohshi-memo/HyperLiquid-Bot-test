# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T15:00:28.837131+00:00`
- Correlation status: `ready`
- Asset price records: `83`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `7`; crypto_alt avg `0.2026` n `223`; crypto_major avg `0.024` n `7`; equity avg `-0.0172` n `42`; fx avg `0.0312` n `4`; index avg `-0.001` n `9`; metal avg `0.0037` n `7`; unknown avg `-0.1073` n `313`
- 1h: commodity avg `-0.0067` n `7`; crypto_alt avg `0.549` n `223`; crypto_major avg `0.0022` n `7`; equity avg `-0.1168` n `42`; fx avg `0.0459` n `4`; index avg `-0.0078` n `9`; metal avg `-0.0071` n `7`; unknown avg `-0.0443` n `313`
- 4h: commodity avg `-0.0753` n `7`; crypto_alt avg `1.117` n `223`; crypto_major avg `0.2827` n `7`; equity avg `-0.0234` n `42`; fx avg `0.0218` n `4`; index avg `0.0353` n `9`; metal avg `-0.0205` n `7`; unknown avg `-0.0262` n `313`
- 24h: commodity avg `0.2848` n `7`; crypto_alt avg `1.0729` n `223`; crypto_major avg `-0.1488` n `7`; equity avg `0.5267` n `42`; fx avg `-0.116` n `4`; index avg `0.072` n `9`; metal avg `-0.3396` n `7`; unknown avg `0.8794` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5381`, n `79`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5364`, n `75`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5334`, n `75`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5195`, n `79`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4782`, n `75`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4755`, n `75`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4654`, n `75`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4568`, n `79`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4406`, n `79`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4252`, n `75`, moderate_sample_signal
