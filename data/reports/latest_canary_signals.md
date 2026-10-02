# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T20:37:34.459089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1625` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7415` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6474` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.59` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.013` n `13`; crypto_alt avg `0.3044` n `235`; crypto_major avg `0.0418` n `8`; equity avg `0.0046` n `143`; fx avg `-0.0011` n `6`; index avg `0.0041` n `26`; metal avg `-0.011` n `20`; unknown avg `19.6014` n `974`
- 1h: commodity avg `0.1681` n `13`; crypto_alt avg `0.1471` n `235`; crypto_major avg `0.0416` n `8`; equity avg `-0.1218` n `143`; fx avg `-0.02` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0377` n `20`; unknown avg `14.6981` n `924`
- 4h: commodity avg `0.5363` n `13`; crypto_alt avg `-3.0184` n `235`; crypto_major avg `-1.6262` n `8`; equity avg `-0.0362` n `143`; fx avg `-0.0067` n `6`; index avg `0.0212` n `26`; metal avg `0.1153` n `20`; unknown avg `4.2576` n `924`
- 24h: commodity avg `0.0367` n `13`; crypto_alt avg `-1.6893` n `235`; crypto_major avg `-1.0208` n `8`; equity avg `0.7385` n `142`; fx avg `-0.1411` n `6`; index avg `0.3044` n `26`; metal avg `-0.2086` n `20`; unknown avg `0.1776` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
