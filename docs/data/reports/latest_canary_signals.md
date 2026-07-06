# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T03:07:28.828747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.74` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `0.0924` n `229`; crypto_major avg `0.0971` n `8`; equity avg `0.2803` n `88`; fx avg `0.0011` n `6`; index avg `0.0653` n `25`; metal avg `-0.0706` n `20`; unknown avg `-0.1254` n `763`
- 1h: commodity avg `-0.1329` n `12`; crypto_alt avg `0.0825` n `229`; crypto_major avg `0.0096` n `8`; equity avg `-0.2477` n `88`; fx avg `-0.001` n `6`; index avg `-0.0542` n `25`; metal avg `-0.1807` n `20`; unknown avg `-0.1521` n `763`
- 4h: commodity avg `-0.0722` n `12`; crypto_alt avg `-0.5154` n `229`; crypto_major avg `-0.4334` n `8`; equity avg `-1.4182` n `88`; fx avg `0.0641` n `6`; index avg `-0.1994` n `25`; metal avg `-0.3911` n `20`; unknown avg `-0.4187` n `763`
- 24h: commodity avg `-0.2463` n `12`; crypto_alt avg `0.7382` n `229`; crypto_major avg `1.7426` n `8`; equity avg `-0.9636` n `88`; fx avg `0.0794` n `6`; index avg `-0.0935` n `25`; metal avg `-0.1852` n `20`; unknown avg `1.0699` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
