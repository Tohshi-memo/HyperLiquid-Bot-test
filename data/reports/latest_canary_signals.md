# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T19:52:31.699583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3906` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.0454` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8714` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7704` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1845` n `13`; crypto_alt avg `-0.2901` n `235`; crypto_major avg `-0.1119` n `8`; equity avg `-0.1789` n `143`; fx avg `-0.0025` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0359` n `20`; unknown avg `4.3866` n `984`
- 1h: commodity avg `0.2358` n `13`; crypto_alt avg `-0.1089` n `235`; crypto_major avg `0.013` n `8`; equity avg `0.0722` n `143`; fx avg `0.0021` n `6`; index avg `0.0421` n `26`; metal avg `0.0648` n `20`; unknown avg `16.2793` n `982`
- 4h: commodity avg `0.5273` n `13`; crypto_alt avg `-3.5624` n `235`; crypto_major avg `-1.8633` n `8`; equity avg `-0.0929` n `143`; fx avg `0.0151` n `6`; index avg `0.0081` n `26`; metal avg `0.1821` n `20`; unknown avg `10.9463` n `976`
- 24h: commodity avg `-0.012` n `13`; crypto_alt avg `-2.1008` n `235`; crypto_major avg `-1.2173` n `8`; equity avg `0.61` n `142`; fx avg `-0.1278` n `6`; index avg `0.2715` n `26`; metal avg `-0.2492` n `20`; unknown avg `103.5814` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
