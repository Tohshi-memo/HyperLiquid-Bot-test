# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T22:22:29.682137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0188` n `229`; crypto_major avg `0.0078` n `8`; equity avg `0.0512` n `91`; fx avg `0.0087` n `6`; index avg `0.0297` n `25`; metal avg `0.0156` n `20`; unknown avg `0.069` n `763`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `-0.08` n `229`; crypto_major avg `-0.2619` n `8`; equity avg `0.0966` n `91`; fx avg `0.021` n `6`; index avg `0.0276` n `25`; metal avg `-0.0051` n `20`; unknown avg `1.0165` n `763`
- 4h: commodity avg `0.0848` n `12`; crypto_alt avg `0.4697` n `229`; crypto_major avg `0.6331` n `8`; equity avg `0.0325` n `91`; fx avg `0.0182` n `6`; index avg `0.0447` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.2358` n `763`
- 24h: commodity avg `0.1455` n `12`; crypto_alt avg `0.5141` n `229`; crypto_major avg `0.0014` n `8`; equity avg `-0.6718` n `90`; fx avg `0.1311` n `6`; index avg `0.0875` n `25`; metal avg `-0.2209` n `20`; unknown avg `-0.4364` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
