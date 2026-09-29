# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T16:52:28.781089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1448` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.141` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.1188` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.0221` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `-0.6653` n `234`; crypto_major avg `-0.6362` n `8`; equity avg `-0.1683` n `142`; fx avg `-0.0069` n `6`; index avg `-0.0325` n `26`; metal avg `-0.0405` n `20`; unknown avg `11.2335` n `962`
- 1h: commodity avg `-0.0653` n `12`; crypto_alt avg `-0.5294` n `234`; crypto_major avg `-0.3428` n `8`; equity avg `-0.1535` n `142`; fx avg `-0.0303` n `6`; index avg `-0.0249` n `26`; metal avg `-0.0328` n `20`; unknown avg `7.7471` n `954`
- 4h: commodity avg `-0.0689` n `12`; crypto_alt avg `-1.7062` n `234`; crypto_major avg `-2.2137` n `8`; equity avg `-0.1916` n `142`; fx avg `-0.0276` n `6`; index avg `-0.0949` n `26`; metal avg `-0.0727` n `20`; unknown avg `4.3751` n `892`
- 24h: commodity avg `-0.5871` n `12`; crypto_alt avg `0.0426` n `234`; crypto_major avg `-1.1321` n `8`; equity avg `0.375` n `142`; fx avg `-0.1725` n `6`; index avg `-0.046` n `26`; metal avg `-0.1396` n `20`; unknown avg `2.4169` n `785`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1902`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
