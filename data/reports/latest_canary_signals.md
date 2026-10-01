# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T10:22:29.845408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0673` n `13`; crypto_alt avg `0.0434` n `234`; crypto_major avg `0.0643` n `8`; equity avg `0.1532` n `142`; fx avg `0.0042` n `6`; index avg `0.0477` n `26`; metal avg `0.1036` n `20`; unknown avg `0.3676` n `975`
- 1h: commodity avg `-0.0606` n `13`; crypto_alt avg `-0.7482` n `234`; crypto_major avg `-0.277` n `8`; equity avg `-0.0735` n `142`; fx avg `-0.0085` n `6`; index avg `0.0074` n `26`; metal avg `0.0615` n `20`; unknown avg `1.334` n `973`
- 4h: commodity avg `0.3216` n `13`; crypto_alt avg `-1.7446` n `234`; crypto_major avg `-1.0391` n `8`; equity avg `-0.7867` n `142`; fx avg `-0.0286` n `6`; index avg `-0.1768` n `26`; metal avg `-0.3439` n `20`; unknown avg `7.9951` n `956`
- 24h: commodity avg `-0.1613` n `13`; crypto_alt avg `-0.9451` n `234`; crypto_major avg `-0.1859` n `8`; equity avg `0.4415` n `142`; fx avg `0.0453` n `6`; index avg `0.1489` n `26`; metal avg `-0.3058` n `20`; unknown avg `774.5209` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
