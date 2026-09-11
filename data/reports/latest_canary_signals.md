# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T18:52:32.680806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.25` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.418` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3021` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0519` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.0102` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0006` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0656` n `12`; crypto_alt avg `-0.4705` n `233`; crypto_major avg `-0.4` n `8`; equity avg `-0.1565` n `136`; fx avg `0.0036` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.1455` n `806`
- 1h: commodity avg `0.1259` n `12`; crypto_alt avg `-1.1547` n `233`; crypto_major avg `-1.042` n `8`; equity avg `-0.4209` n `136`; fx avg `0.0042` n `6`; index avg `-0.0414` n `26`; metal avg `-0.0881` n `20`; unknown avg `0.1914` n `804`
- 4h: commodity avg `0.1441` n `12`; crypto_alt avg `-2.1973` n `233`; crypto_major avg `-2.2739` n `8`; equity avg `-0.2637` n `136`; fx avg `0.0139` n `6`; index avg `0.0282` n `26`; metal avg `-0.222` n `20`; unknown avg `2.3348` n `752`
- 24h: commodity avg `-0.3032` n `12`; crypto_alt avg `-0.4081` n `233`; crypto_major avg `0.5869` n `8`; equity avg `0.3173` n `136`; fx avg `-0.1414` n `6`; index avg `0.2952` n `26`; metal avg `0.1369` n `20`; unknown avg `1.4269` n `666`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
