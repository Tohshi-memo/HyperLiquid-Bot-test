# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T22:37:25.901012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.5044` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.1432` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.081` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.7265` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.5408` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.5223` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8449` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.8312` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0042` n `13`; crypto_alt avg `-0.4423` n `239`; crypto_major avg `-0.5211` n `8`; equity avg `-0.2512` n `158`; fx avg `0.0109` n `6`; index avg `-0.0492` n `27`; metal avg `-0.0235` n `20`; unknown avg `0.7156` n `1260`
- 1h: commodity avg `0.0982` n `13`; crypto_alt avg `-2.1923` n `239`; crypto_major avg `-2.6283` n `8`; equity avg `-0.7971` n `158`; fx avg `-0.0103` n `6`; index avg `-0.0875` n `27`; metal avg `-0.106` n `20`; unknown avg `1.5933` n `1236`
- 4h: commodity avg `0.2539` n `13`; crypto_alt avg `-2.7818` n `239`; crypto_major avg `-3.2505` n `8`; equity avg `-1.4056` n `158`; fx avg `-0.0266` n `6`; index avg `-0.1695` n `27`; metal avg `-0.1073` n `20`; unknown avg `1.9862` n `1188`
- 24h: commodity avg `0.0866` n `13`; crypto_alt avg `-3.8704` n `239`; crypto_major avg `-3.1926` n `8`; equity avg `-0.7868` n `158`; fx avg `0.0345` n `6`; index avg `-0.1506` n `27`; metal avg `-0.1348` n `20`; unknown avg `0.5612` n `1014`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
