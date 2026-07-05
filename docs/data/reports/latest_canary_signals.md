# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T03:07:28.386961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3498` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `0.1772` n `229`; crypto_major avg `0.2351` n `8`; equity avg `0.056` n `88`; fx avg `0.0` n `6`; index avg `-0.0236` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.0019` n `765`
- 1h: commodity avg `0.0256` n `12`; crypto_alt avg `-0.1984` n `229`; crypto_major avg `-0.1559` n `8`; equity avg `0.0377` n `88`; fx avg `-0.0001` n `6`; index avg `-0.0138` n `25`; metal avg `-0.0183` n `20`; unknown avg `-0.3655` n `765`
- 4h: commodity avg `0.0186` n `12`; crypto_alt avg `-1.1118` n `229`; crypto_major avg `-1.3689` n `8`; equity avg `0.0156` n `88`; fx avg `0.0039` n `6`; index avg `-0.0191` n `25`; metal avg `-0.0153` n `20`; unknown avg `-0.4727` n `763`
- 24h: commodity avg `0.0535` n `12`; crypto_alt avg `-0.6959` n `229`; crypto_major avg `-0.5377` n `8`; equity avg `0.1837` n `88`; fx avg `0.0198` n `6`; index avg `0.0252` n `25`; metal avg `0.0858` n `20`; unknown avg `-0.9386` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
