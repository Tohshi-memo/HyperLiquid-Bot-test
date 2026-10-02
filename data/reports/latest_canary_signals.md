# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T20:07:29.071477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2867` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.0013` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8229` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.721` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0271` n `13`; crypto_alt avg `0.1253` n `235`; crypto_major avg `0.1119` n `8`; equity avg `0.0582` n `143`; fx avg `-0.0012` n `6`; index avg `0.0157` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.8762` n `962`
- 1h: commodity avg `0.2167` n `13`; crypto_alt avg `-0.0005` n `235`; crypto_major avg `-0.0297` n `8`; equity avg `0.161` n `143`; fx avg `0.0023` n `6`; index avg `0.0461` n `26`; metal avg `0.0513` n `20`; unknown avg `3.44` n `962`
- 4h: commodity avg `0.4701` n `13`; crypto_alt avg `-3.6507` n `235`; crypto_major avg `-1.8166` n `8`; equity avg `-0.0956` n `143`; fx avg `0.0006` n `6`; index avg `0.0063` n `26`; metal avg `0.1847` n `20`; unknown avg `4.0291` n `962`
- 24h: commodity avg `-0.0417` n `13`; crypto_alt avg `-1.9432` n `235`; crypto_major avg `-1.18` n `8`; equity avg `0.793` n `142`; fx avg `-0.1392` n `6`; index avg `0.3049` n `26`; metal avg `-0.2205` n `20`; unknown avg `102.176` n `812`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
