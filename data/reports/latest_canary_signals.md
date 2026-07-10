# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T07:37:27.334039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.0172` n `229`; crypto_major avg `-0.0975` n `8`; equity avg `0.0126` n `91`; fx avg `0.0098` n `6`; index avg `-0.0037` n `25`; metal avg `-0.0452` n `20`; unknown avg `-0.0065` n `765`
- 1h: commodity avg `-0.1777` n `12`; crypto_alt avg `0.0229` n `229`; crypto_major avg `-0.0293` n `8`; equity avg `-0.2009` n `91`; fx avg `0.0072` n `6`; index avg `-0.0145` n `25`; metal avg `-0.0202` n `20`; unknown avg `0.9849` n `765`
- 4h: commodity avg `-0.2726` n `12`; crypto_alt avg `-0.1633` n `229`; crypto_major avg `-0.0943` n `8`; equity avg `-0.7122` n `91`; fx avg `-0.0769` n `6`; index avg `-0.1376` n `25`; metal avg `-0.0901` n `20`; unknown avg `-0.0851` n `733`
- 24h: commodity avg `-0.9416` n `12`; crypto_alt avg `0.6855` n `229`; crypto_major avg `0.8708` n `8`; equity avg `0.2799` n `91`; fx avg `-0.1161` n `6`; index avg `0.1676` n `25`; metal avg `0.2579` n `20`; unknown avg `0.1231` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
