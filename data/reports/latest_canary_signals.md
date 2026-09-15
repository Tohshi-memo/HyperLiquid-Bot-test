# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T00:22:31.952890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.4702` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.424` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3969` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1803` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0709` n `12`; crypto_alt avg `-0.03` n `233`; crypto_major avg `-0.0622` n `8`; equity avg `0.1155` n `136`; fx avg `0.033` n `6`; index avg `0.048` n `27`; metal avg `-0.0584` n `20`; unknown avg `1.671` n `908`
- 1h: commodity avg `0.0463` n `12`; crypto_alt avg `-0.0824` n `233`; crypto_major avg `-0.3025` n `8`; equity avg `0.1294` n `136`; fx avg `0.0505` n `6`; index avg `0.0704` n `27`; metal avg `-0.1021` n `20`; unknown avg `0.7685` n `906`
- 4h: commodity avg `0.1248` n `12`; crypto_alt avg `-1.4901` n `233`; crypto_major avg `-2.2992` n `8`; equity avg `0.171` n `136`; fx avg `0.0287` n `6`; index avg `0.0977` n `27`; metal avg `-0.1189` n `20`; unknown avg `3.5872` n `878`
- 24h: commodity avg `-0.0528` n `12`; crypto_alt avg `1.1868` n `233`; crypto_major avg `2.146` n `8`; equity avg `0.0895` n `136`; fx avg `0.0502` n `6`; index avg `0.0474` n `27`; metal avg `-0.4903` n `20`; unknown avg `6.5442` n `676`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
