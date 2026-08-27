# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T04:52:25.482804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `-0.0868` n `231`; crypto_major avg `0.0161` n `8`; equity avg `-0.0452` n `126`; fx avg `0.0029` n `6`; index avg `-0.0166` n `25`; metal avg `0.0211` n `20`; unknown avg `-0.1043` n `793`
- 1h: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.3094` n `231`; crypto_major avg `-0.1905` n `8`; equity avg `-0.1323` n `126`; fx avg `0.0026` n `6`; index avg `-0.0431` n `25`; metal avg `-0.0427` n `20`; unknown avg `-0.3151` n `793`
- 4h: commodity avg `0.0381` n `12`; crypto_alt avg `-0.5735` n `231`; crypto_major avg `-0.2985` n `8`; equity avg `0.4105` n `126`; fx avg `0.0365` n `6`; index avg `0.0297` n `25`; metal avg `0.1048` n `20`; unknown avg `-0.1016` n `793`
- 24h: commodity avg `0.4229` n `12`; crypto_alt avg `0.0542` n `231`; crypto_major avg `0.2307` n `8`; equity avg `1.0203` n `126`; fx avg `-0.0992` n `6`; index avg `0.1225` n `25`; metal avg `-0.2359` n `20`; unknown avg `0.2323` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
