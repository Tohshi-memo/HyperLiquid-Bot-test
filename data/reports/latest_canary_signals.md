# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T13:37:28.191211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.02` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-2.2293` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.2142` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.007` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9813` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1864` n `12`; crypto_alt avg `0.0635` n `232`; crypto_major avg `-0.0373` n `8`; equity avg `0.6513` n `133`; fx avg `-0.02` n `6`; index avg `0.1142` n `26`; metal avg `0.1052` n `20`; unknown avg `-0.2243` n `793`
- 1h: commodity avg `-0.2237` n `12`; crypto_alt avg `0.1807` n `232`; crypto_major avg `0.1037` n `8`; equity avg `0.7907` n `133`; fx avg `-0.0994` n `6`; index avg `0.1128` n `26`; metal avg `0.2338` n `20`; unknown avg `22.3147` n `749`
- 4h: commodity avg `-0.1717` n `12`; crypto_alt avg `-1.8421` n `232`; crypto_major avg `-2.1787` n `8`; equity avg `0.0506` n `133`; fx avg `-0.1876` n `6`; index avg `0.0355` n `26`; metal avg `-0.1974` n `20`; unknown avg `-0.1827` n `743`
- 24h: commodity avg `-0.5164` n `12`; crypto_alt avg `0.6817` n `232`; crypto_major avg `1.1329` n `8`; equity avg `2.1869` n `133`; fx avg `-0.1305` n `6`; index avg `0.3429` n `26`; metal avg `-0.0184` n `20`; unknown avg `28.6719` n `704`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
