# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T03:22:21.816985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2251` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.6787` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5183` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `0.172` n `228`; crypto_major avg `0.2845` n `8`; equity avg `0.0886` n `74`; fx avg `0.0001` n `6`; index avg `0.0046` n `23`; metal avg `0.0104` n `18`; unknown avg `0.2569` n `516`
- 1h: commodity avg `-0.0631` n `12`; crypto_alt avg `0.2672` n `228`; crypto_major avg `0.6795` n `8`; equity avg `0.1405` n `74`; fx avg `-0.0013` n `6`; index avg `0.1705` n `23`; metal avg `0.1623` n `18`; unknown avg `0.3553` n `516`
- 4h: commodity avg `-0.0338` n `12`; crypto_alt avg `2.1876` n `228`; crypto_major avg `2.1913` n `8`; equity avg `0.673` n `74`; fx avg `-0.0025` n `6`; index avg `0.2343` n `23`; metal avg `0.5126` n `18`; unknown avg `1.1401` n `515`
- 24h: commodity avg `-0.0627` n `12`; crypto_alt avg `1.9709` n `228`; crypto_major avg `1.2962` n `8`; equity avg `1.6872` n `74`; fx avg `0.058` n `6`; index avg `0.852` n `23`; metal avg `0.4547` n `18`; unknown avg `0.2276` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
