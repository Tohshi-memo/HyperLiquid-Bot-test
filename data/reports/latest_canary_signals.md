# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T04:52:28.790454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3573` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0755` n `12`; crypto_alt avg `0.0446` n `230`; crypto_major avg `0.0486` n `8`; equity avg `0.0137` n `102`; fx avg `0.003` n `6`; index avg `0.0077` n `25`; metal avg `0.0023` n `20`; unknown avg `0.4274` n `782`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `0.1963` n `230`; crypto_major avg `0.1665` n `8`; equity avg `0.0867` n `102`; fx avg `0.0013` n `6`; index avg `-0.0089` n `25`; metal avg `0.0177` n `20`; unknown avg `0.2861` n `782`
- 4h: commodity avg `-1.0243` n `12`; crypto_alt avg `1.023` n `230`; crypto_major avg `1.333` n `8`; equity avg `0.7571` n `102`; fx avg `-0.0393` n `6`; index avg `0.1898` n `25`; metal avg `0.187` n `20`; unknown avg `2.2351` n `782`
- 24h: commodity avg `-1.1124` n `12`; crypto_alt avg `0.0537` n `230`; crypto_major avg `0.3092` n `8`; equity avg `0.8617` n `102`; fx avg `-0.0984` n `6`; index avg `0.1925` n `25`; metal avg `0.2733` n `20`; unknown avg `0.0203` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
