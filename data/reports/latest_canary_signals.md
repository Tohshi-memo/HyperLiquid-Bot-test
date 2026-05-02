# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T11:30:20.790275+00:00`
- Correlation status: `ready`
- Asset price records: `69`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.047` n `7`; crypto_alt avg `0.0371` n `223`; crypto_major avg `0.0539` n `7`; equity avg `0.0276` n `42`; fx avg `-0.0005` n `4`; index avg `0.007` n `9`; metal avg `-0.0049` n `7`; unknown avg `-0.0204` n `313`
- 1h: commodity avg `-0.0123` n `7`; crypto_alt avg `-0.1058` n `223`; crypto_major avg `-0.0006` n `7`; equity avg `-0.0093` n `42`; fx avg `-0.0144` n `4`; index avg `0.0138` n `9`; metal avg `-0.0061` n `7`; unknown avg `0.0347` n `313`
- 4h: commodity avg `0.0375` n `7`; crypto_alt avg `0.1579` n `223`; crypto_major avg `0.0433` n `7`; equity avg `-0.0429` n `42`; fx avg `0.028` n `4`; index avg `0.0054` n `9`; metal avg `0.0466` n `7`; unknown avg `0.2739` n `311`
- 24h: crypto_alt avg `0.7623` n `223`; crypto_major avg `0.6646` n `7`; metal avg `0.7818` n `1`; unknown avg `1.413` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5748`, n `65`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5563`, n `61`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5548`, n `65`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5448`, n `61`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4787`, n `65`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4761`, n `61`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4731`, n `61`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4625`, n `61`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4448`, n `65`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4363`, n `65`, moderate_sample_signal
