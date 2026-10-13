# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T05:22:38.387956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.365` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9401` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5831` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0288` n `13`; crypto_alt avg `0.1863` n `235`; crypto_major avg `0.1532` n `8`; equity avg `0.3714` n `151`; fx avg `0.0282` n `6`; index avg `0.0631` n `26`; metal avg `-0.0008` n `20`; unknown avg `27.293` n `1135`
- 1h: commodity avg `0.0299` n `13`; crypto_alt avg `0.8624` n `235`; crypto_major avg `0.4117` n `8`; equity avg `0.3837` n `151`; fx avg `0.0361` n `6`; index avg `0.0801` n `26`; metal avg `0.0538` n `20`; unknown avg `9.9447` n `1129`
- 4h: commodity avg `-0.2012` n `13`; crypto_alt avg `2.7507` n `235`; crypto_major avg `2.1638` n `8`; equity avg `0.5807` n `151`; fx avg `0.1007` n `6`; index avg `0.0437` n `26`; metal avg `0.2237` n `20`; unknown avg `6.4274` n `1091`
- 24h: commodity avg `0.4728` n `13`; crypto_alt avg `-4.112` n `235`; crypto_major avg `-2.4665` n `8`; equity avg `-3.4654` n `151`; fx avg `0.035` n `6`; index avg `-0.488` n `26`; metal avg `0.0135` n `20`; unknown avg `0.4983` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2016`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1893`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1356`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0863`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `666`, weak_sample_signal
