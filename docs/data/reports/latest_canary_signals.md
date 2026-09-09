# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T22:38:01.478539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2074` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0698` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9439` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5249` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `-0.0249` n `233`; crypto_major avg `-0.0583` n `8`; equity avg `-0.008` n `134`; fx avg `-0.0035` n `6`; index avg `0.0002` n `26`; metal avg `0.0004` n `20`; unknown avg `1.0862` n `787`
- 1h: commodity avg `0.0415` n `12`; crypto_alt avg `-1.6326` n `233`; crypto_major avg `-0.8265` n `8`; equity avg `-0.1547` n `134`; fx avg `-0.0191` n `6`; index avg `0.0015` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.7344` n `735`
- 4h: commodity avg `0.1307` n `12`; crypto_alt avg `-3.4041` n `233`; crypto_major avg `-2.0767` n `8`; equity avg `-0.5518` n `134`; fx avg `-0.0139` n `6`; index avg `-0.0069` n `26`; metal avg `-0.1328` n `20`; unknown avg `21.2254` n `691`
- 24h: commodity avg `0.1453` n `12`; crypto_alt avg `-3.3596` n `233`; crypto_major avg `-2.0796` n `8`; equity avg `-0.6148` n `134`; fx avg `-0.0254` n `6`; index avg `-0.1112` n `26`; metal avg `0.5441` n `20`; unknown avg `1.482` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
