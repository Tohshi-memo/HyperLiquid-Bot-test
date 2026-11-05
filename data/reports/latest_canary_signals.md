# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T19:05:06.246645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1383` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9177` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6817` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.006` n `13`; crypto_alt avg `-0.1339` n `239`; crypto_major avg `-0.1635` n `8`; equity avg `0.0033` n `158`; fx avg `0.0028` n `6`; index avg `-0.0281` n `27`; metal avg `-0.0155` n `20`; unknown avg `6.3637` n `1252`
- 1h: commodity avg `-0.094` n `13`; crypto_alt avg `0.9656` n `239`; crypto_major avg `0.253` n `8`; equity avg `0.3279` n `158`; fx avg `-0.0169` n `6`; index avg `-0.0173` n `27`; metal avg `0.0064` n `20`; unknown avg `6.5272` n `1252`
- 4h: commodity avg `0.0311` n `13`; crypto_alt avg `-1.8582` n `239`; crypto_major avg `-2.1072` n `8`; equity avg `-2.7014` n `158`; fx avg `0.0567` n `6`; index avg `-0.4255` n `27`; metal avg `-0.1895` n `20`; unknown avg `8.0415` n `1244`
- 24h: commodity avg `0.6961` n `13`; crypto_alt avg `-4.9346` n `239`; crypto_major avg `-5.332` n `8`; equity avg `-8.2943` n `158`; fx avg `0.1119` n `6`; index avg `-1.1322` n `27`; metal avg `0.2248` n `20`; unknown avg `240.2717` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
