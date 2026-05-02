# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T09:30:23.705851+00:00`
- Correlation status: `ready`
- Asset price records: `61`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `7`; crypto_alt avg `-0.0451` n `223`; crypto_major avg `-0.1093` n `7`; equity avg `-0.0107` n `42`; fx avg `0.0125` n `4`; index avg `0.0305` n `9`; metal avg `0.0059` n `7`; unknown avg `-0.0419` n `313`
- 1h: commodity avg `0.0121` n `7`; crypto_alt avg `0.2856` n `223`; crypto_major avg `0.0361` n `7`; equity avg `-0.1293` n `42`; fx avg `0.0173` n `4`; index avg `0.0188` n `9`; metal avg `0.0154` n `7`; unknown avg `0.0553` n `313`
- 4h: commodity avg `0.0453` n `7`; crypto_alt avg `0.6461` n `223`; crypto_major avg `0.3573` n `7`; equity avg `0.1327` n `42`; fx avg `0.025` n `4`; index avg `0.0118` n `9`; metal avg `0.0885` n `7`; unknown avg `0.1979` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5795`, n `57`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5719`, n `53`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5596`, n `53`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5593`, n `57`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4818`, n `53`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4728`, n `57`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4683`, n `53`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4552`, n `53`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4411`, n `57`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4388`, n `57`, moderate_sample_signal
