# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T08:37:25.910754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1468` n `12`; crypto_alt avg `-0.3525` n `229`; crypto_major avg `-0.4435` n `8`; equity avg `-1.0737` n `91`; fx avg `0.0274` n `6`; index avg `-0.1711` n `25`; metal avg `-0.2543` n `20`; unknown avg `-0.0636` n `763`
- 1h: commodity avg `0.6571` n `12`; crypto_alt avg `-1.0678` n `229`; crypto_major avg `-1.1238` n `8`; equity avg `-1.6502` n `91`; fx avg `0.0607` n `6`; index avg `-0.3144` n `25`; metal avg `-0.6129` n `20`; unknown avg `-0.0665` n `763`
- 4h: commodity avg `0.6692` n `12`; crypto_alt avg `-0.9807` n `229`; crypto_major avg `-1.1726` n `8`; equity avg `-1.6436` n `91`; fx avg `0.0107` n `6`; index avg `-0.364` n `25`; metal avg `-0.7034` n `20`; unknown avg `-0.3654` n `743`
- 24h: commodity avg `1.3623` n `12`; crypto_alt avg `-3.5501` n `229`; crypto_major avg `-3.1761` n `8`; equity avg `-3.2027` n `91`; fx avg `-0.157` n `6`; index avg `-0.6819` n `25`; metal avg `-0.7905` n `20`; unknown avg `-0.7654` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
