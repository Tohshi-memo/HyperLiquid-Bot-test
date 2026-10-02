# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T15:22:46.463068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.62` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.5472` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4576` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1355` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0925` n `13`; crypto_alt avg `0.2094` n `235`; crypto_major avg `0.0196` n `8`; equity avg `-0.282` n `143`; fx avg `-0.0065` n `6`; index avg `-0.0612` n `26`; metal avg `-0.0495` n `20`; unknown avg `0.0564` n `984`
- 1h: commodity avg `0.3284` n `13`; crypto_alt avg `-1.0009` n `235`; crypto_major avg `-1.3011` n `8`; equity avg `-0.8089` n `143`; fx avg `0.0137` n `6`; index avg `-0.1656` n `26`; metal avg `-0.3603` n `20`; unknown avg `2.5674` n `958`
- 4h: commodity avg `0.2305` n `13`; crypto_alt avg `-0.2601` n `235`; crypto_major avg `-1.4004` n `8`; equity avg `0.1468` n `142`; fx avg `0.0355` n `6`; index avg `0.0572` n `26`; metal avg `-0.3585` n `20`; unknown avg `0.823` n `934`
- 24h: commodity avg `-0.6592` n `13`; crypto_alt avg `2.1322` n `235`; crypto_major avg `0.8938` n `8`; equity avg `1.7368` n `142`; fx avg `-0.1516` n `6`; index avg `0.4624` n `26`; metal avg `-0.1665` n `20`; unknown avg `101.0793` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
