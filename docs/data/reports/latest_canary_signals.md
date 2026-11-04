# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T15:37:36.563710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.2213` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `2.5663` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.3356` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.2324` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `2.1733` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0286` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1296` n `13`; crypto_alt avg `0.018` n `239`; crypto_major avg `-0.085` n `8`; equity avg `-0.1258` n `158`; fx avg `-0.0076` n `6`; index avg `0.014` n `27`; metal avg `0.0537` n `20`; unknown avg `4.0147` n `1262`
- 1h: commodity avg `0.3357` n `13`; crypto_alt avg `2.424` n `239`; crypto_major avg `2.5681` n `8`; equity avg `0.2325` n `158`; fx avg `-0.0242` n `6`; index avg `0.0636` n `27`; metal avg `0.0018` n `20`; unknown avg `1.1437` n `1256`
- 4h: commodity avg `-0.1252` n `13`; crypto_alt avg `1.5106` n `239`; crypto_major avg `2.0481` n `8`; equity avg `-1.1732` n `158`; fx avg `0.0007` n `6`; index avg `0.0245` n `27`; metal avg `0.0195` n `20`; unknown avg `0.959` n `1252`
- 24h: commodity avg `-0.3096` n `13`; crypto_alt avg `3.3519` n `239`; crypto_major avg `3.0866` n `8`; equity avg `0.1481` n `158`; fx avg `0.1127` n `6`; index avg `0.1663` n `27`; metal avg `0.9265` n `20`; unknown avg `0.5852` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2606`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
