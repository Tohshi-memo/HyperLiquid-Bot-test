# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T14:22:31.858535+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6596` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.338` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0204` n `12`; crypto_alt avg `0.0021` n `229`; crypto_major avg `-0.0555` n `8`; equity avg `0.0931` n `88`; fx avg `0.0011` n `6`; index avg `0.0311` n `25`; metal avg `0.0216` n `20`; unknown avg `-0.0087` n `765`
- 1h: commodity avg `0.0672` n `12`; crypto_alt avg `0.8` n `229`; crypto_major avg `0.5302` n `8`; equity avg `0.938` n `88`; fx avg `-0.0065` n `6`; index avg `0.1154` n `25`; metal avg `0.0682` n `20`; unknown avg `0.0752` n `765`
- 4h: commodity avg `0.0991` n `12`; crypto_alt avg `-0.5009` n `229`; crypto_major avg `-1.237` n `8`; equity avg `0.4226` n `88`; fx avg `0.0252` n `6`; index avg `0.101` n `25`; metal avg `-0.1418` n `20`; unknown avg `-0.2405` n `765`
- 24h: commodity avg `-0.028` n `12`; crypto_alt avg `-0.6811` n `229`; crypto_major avg `-1.1553` n `8`; equity avg `-0.1754` n `88`; fx avg `0.1701` n `6`; index avg `0.0734` n `25`; metal avg `-0.3716` n `20`; unknown avg `0.5824` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
