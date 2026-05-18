# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T01:37:15.079967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.6033` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8168` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5302` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0781` n `12`; crypto_alt avg `-0.2422` n `228`; crypto_major avg `-0.1863` n `8`; equity avg `0.0086` n `66`; fx avg `0.0277` n `5`; index avg `-0.0276` n `23`; metal avg `0.0316` n `18`; unknown avg `-0.2337` n `383`
- 1h: commodity avg `0.5665` n `12`; crypto_alt avg `-0.1829` n `228`; crypto_major avg `-0.4549` n `8`; equity avg `0.0704` n `66`; fx avg `0.0433` n `5`; index avg `0.0295` n `23`; metal avg `-0.1185` n `18`; unknown avg `-0.1537` n `383`
- 4h: commodity avg `1.2157` n `12`; crypto_alt avg `-2.8285` n `228`; crypto_major avg `-2.3876` n `8`; equity avg `-0.8574` n `66`; fx avg `0.0867` n `5`; index avg `-0.5708` n `23`; metal avg `-0.9092` n `18`; unknown avg `2.2607` n `383`
- 24h: commodity avg `2.9065` n `12`; crypto_alt avg `-11.3596` n `228`; crypto_major avg `-3.4631` n `8`; equity avg `-3.6397` n `65`; fx avg `-0.0924` n `5`; index avg `-2.0089` n `23`; metal avg `-6.747` n `18`; unknown avg `550.0929` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
