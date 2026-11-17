# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T16:52:55.568222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0215` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7577` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.651` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0047` n `13`; crypto_alt avg `-0.3406` n `239`; crypto_major avg `-0.2246` n `8`; equity avg `-0.3873` n `163`; fx avg `0.0125` n `6`; index avg `-0.0575` n `27`; metal avg `-0.061` n `20`; unknown avg `0.2377` n `1265`
- 1h: commodity avg `0.0225` n `13`; crypto_alt avg `0.5412` n `239`; crypto_major avg `0.5938` n `8`; equity avg `0.8482` n `163`; fx avg `0.0093` n `6`; index avg `0.0699` n `27`; metal avg `-0.0797` n `20`; unknown avg `1.5662` n `1249`
- 4h: commodity avg `0.0676` n `13`; crypto_alt avg `-1.8988` n `239`; crypto_major avg `-1.9539` n `8`; equity avg `-2.886` n `163`; fx avg `0.0355` n `6`; index avg `-0.3029` n `27`; metal avg `-0.1962` n `20`; unknown avg `11.1247` n `1207`
- 24h: commodity avg `-0.0746` n `13`; crypto_alt avg `-0.6002` n `239`; crypto_major avg `-0.6081` n `8`; equity avg `-3.293` n `163`; fx avg `0.0061` n `6`; index avg `-0.4179` n `27`; metal avg `-0.0836` n `20`; unknown avg `8.3704` n `1098`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
