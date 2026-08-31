# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T00:07:24.969289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.7795` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.7558` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.584` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1797` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0509` n `12`; crypto_alt avg `0.2785` n `231`; crypto_major avg `-0.0422` n `8`; equity avg `-0.403` n `128`; fx avg `0.0048` n `6`; index avg `-0.0998` n `26`; metal avg `0.0414` n `20`; unknown avg `0.221` n `791`
- 1h: commodity avg `-0.119` n `12`; crypto_alt avg `-1.7323` n `231`; crypto_major avg `-1.4406` n `8`; equity avg `-0.9864` n `128`; fx avg `0.0084` n `6`; index avg `-0.2609` n `26`; metal avg `-0.1142` n `20`; unknown avg `1.4659` n `791`
- 4h: commodity avg `-0.23` n `12`; crypto_alt avg `-2.975` n `231`; crypto_major avg `-2.9858` n `8`; equity avg `-1.5285` n `128`; fx avg `0.0183` n `6`; index avg `-0.4018` n `26`; metal avg `-0.2063` n `20`; unknown avg `2.5911` n `789`
- 24h: commodity avg `0.1808` n `12`; crypto_alt avg `-1.5138` n `231`; crypto_major avg `-2.3146` n `8`; equity avg `-1.4235` n `128`; fx avg `0.0286` n `6`; index avg `-0.3567` n `26`; metal avg `-0.1347` n `20`; unknown avg `-0.4617` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0443`, n `668`, weak_sample_signal
