# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T19:37:49.959050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2227` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.8598` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.8547` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7635` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0418` n `13`; crypto_alt avg `0.4961` n `235`; crypto_major avg `0.3046` n `8`; equity avg `0.2176` n `143`; fx avg `0.0024` n `6`; index avg `0.037` n `26`; metal avg `0.0337` n `20`; unknown avg `14.0572` n `984`
- 1h: commodity avg `0.0413` n `13`; crypto_alt avg `-0.6056` n `235`; crypto_major avg `-0.4535` n `8`; equity avg `0.3012` n `143`; fx avg `0.0064` n `6`; index avg `0.0571` n `26`; metal avg `0.1007` n `20`; unknown avg `19.3259` n `982`
- 4h: commodity avg `0.4948` n `13`; crypto_alt avg `-3.3447` n `235`; crypto_major avg `-1.7279` n `8`; equity avg `0.1319` n `143`; fx avg `0.0094` n `6`; index avg `0.0356` n `26`; metal avg `0.1268` n `20`; unknown avg `8.2246` n `976`
- 24h: commodity avg `-0.212` n `13`; crypto_alt avg `-1.1748` n `235`; crypto_major avg `-0.7849` n `8`; equity avg `0.9341` n `142`; fx avg `-0.1263` n `6`; index avg `0.3184` n `26`; metal avg `-0.1924` n `20`; unknown avg `104.1393` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
