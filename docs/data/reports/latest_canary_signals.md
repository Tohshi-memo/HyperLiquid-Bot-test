# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T18:37:28.974628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2387` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1906` n `12`; crypto_alt avg `0.0929` n `233`; crypto_major avg `0.195` n `8`; equity avg `-0.021` n `136`; fx avg `-0.0105` n `6`; index avg `0.0142` n `27`; metal avg `0.0175` n `20`; unknown avg `0.3974` n `908`
- 1h: commodity avg `-0.1635` n `12`; crypto_alt avg `0.5308` n `233`; crypto_major avg `0.887` n `8`; equity avg `-0.0512` n `136`; fx avg `-0.0096` n `6`; index avg `0.0121` n `27`; metal avg `0.0308` n `20`; unknown avg `3.5837` n `906`
- 4h: commodity avg `-0.5093` n `12`; crypto_alt avg `1.4548` n `233`; crypto_major avg `1.7294` n `8`; equity avg `0.9877` n `136`; fx avg `-0.0005` n `6`; index avg `0.2071` n `27`; metal avg `0.2807` n `20`; unknown avg `0.5182` n `864`
- 24h: commodity avg `0.09` n `12`; crypto_alt avg `0.4288` n `233`; crypto_major avg `2.4952` n `8`; equity avg `-0.2797` n `136`; fx avg `0.0526` n `6`; index avg `-0.1134` n `27`; metal avg `-0.2916` n `20`; unknown avg `1.4968` n `688`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
