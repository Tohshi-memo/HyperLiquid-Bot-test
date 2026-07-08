# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T11:37:26.708303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0416` n `12`; crypto_alt avg `0.2607` n `229`; crypto_major avg `0.0707` n `8`; equity avg `0.0581` n `91`; fx avg `-0.0081` n `6`; index avg `0.0172` n `25`; metal avg `-0.0383` n `20`; unknown avg `0.0087` n `763`
- 1h: commodity avg `0.1122` n `12`; crypto_alt avg `0.3713` n `229`; crypto_major avg `-0.012` n `8`; equity avg `-0.0441` n `91`; fx avg `0.0231` n `6`; index avg `0.0097` n `25`; metal avg `-0.1044` n `20`; unknown avg `-0.0292` n `763`
- 4h: commodity avg `0.5983` n `12`; crypto_alt avg `-0.7635` n `229`; crypto_major avg `-0.731` n `8`; equity avg `-1.5523` n `91`; fx avg `0.0319` n `6`; index avg `-0.3126` n `25`; metal avg `-1.0968` n `20`; unknown avg `-0.1061` n `763`
- 24h: commodity avg `1.3542` n `12`; crypto_alt avg `-3.5401` n `229`; crypto_major avg `-2.9028` n `8`; equity avg `-2.7265` n `91`; fx avg `-0.0969` n `6`; index avg `-0.576` n `25`; metal avg `-1.4203` n `20`; unknown avg `-0.8553` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
