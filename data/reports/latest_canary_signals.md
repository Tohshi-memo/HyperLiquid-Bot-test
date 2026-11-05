# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T16:22:39.935688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.8277` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.4916` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.9818` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0736` n `13`; crypto_alt avg `1.1982` n `239`; crypto_major avg `0.9914` n `8`; equity avg `2.5944` n `158`; fx avg `-0.0002` n `6`; index avg `0.1789` n `27`; metal avg `0.2659` n `20`; unknown avg `2.9077` n `1256`
- 1h: commodity avg `0.0655` n `13`; crypto_alt avg `0.0584` n `239`; crypto_major avg `0.2819` n `8`; equity avg `0.3973` n `158`; fx avg `0.0128` n `6`; index avg `-0.0424` n `27`; metal avg `0.0686` n `20`; unknown avg `2.4948` n `1248`
- 4h: commodity avg `0.3043` n `13`; crypto_alt avg `-3.761` n `239`; crypto_major avg `-3.5234` n `8`; equity avg `-4.9648` n `158`; fx avg `0.0465` n `6`; index avg `-0.5416` n `27`; metal avg `-0.0318` n `20`; unknown avg `8.1881` n `1245`
- 24h: commodity avg `-0.0424` n `13`; crypto_alt avg `-5.3041` n `239`; crypto_major avg `-4.686` n `8`; equity avg `-6.1283` n `158`; fx avg `0.0794` n `6`; index avg `-0.7787` n `27`; metal avg `0.5737` n `20`; unknown avg `210.2938` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.24`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
