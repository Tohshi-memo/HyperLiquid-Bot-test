# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T18:52:34.022957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0991` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.8738` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.5156` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.144` n `13`; crypto_alt avg `0.0741` n `239`; crypto_major avg `0.0177` n `8`; equity avg `-0.1291` n `158`; fx avg `-0.0208` n `6`; index avg `-0.0154` n `27`; metal avg `-0.0364` n `20`; unknown avg `0.1196` n `1256`
- 1h: commodity avg `-0.1011` n `13`; crypto_alt avg `0.7457` n `239`; crypto_major avg `0.1414` n `8`; equity avg `-0.1041` n `158`; fx avg `-0.0199` n `6`; index avg `-0.0395` n `27`; metal avg `-0.0124` n `20`; unknown avg `0.3408` n `1254`
- 4h: commodity avg `0.1183` n `13`; crypto_alt avg `-2.6311` n `239`; crypto_major avg `-2.9808` n `8`; equity avg `-3.065` n `158`; fx avg `0.0422` n `6`; index avg `-0.4652` n `27`; metal avg `-0.107` n `20`; unknown avg `3.5787` n `1246`
- 24h: commodity avg `0.6423` n `13`; crypto_alt avg `-4.755` n `239`; crypto_major avg `-5.205` n `8`; equity avg `-8.0894` n `158`; fx avg `0.1053` n `6`; index avg `-1.0758` n `27`; metal avg `0.2524` n `20`; unknown avg `213.769` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1837`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
