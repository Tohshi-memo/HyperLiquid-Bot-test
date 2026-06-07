# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T23:52:25.839241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4831` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4924` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2328` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0541` n `12`; crypto_alt avg `-0.1223` n `228`; crypto_major avg `-0.0308` n `8`; equity avg `0.025` n `74`; fx avg `-0.0107` n `6`; index avg `0.0316` n `23`; metal avg `0.0897` n `18`; unknown avg `0.1732` n `517`
- 1h: commodity avg `-0.1587` n `12`; crypto_alt avg `-0.4593` n `228`; crypto_major avg `-0.086` n `8`; equity avg `-0.1501` n `74`; fx avg `-0.005` n `6`; index avg `0.1207` n `23`; metal avg `0.338` n `18`; unknown avg `-0.0049` n `516`
- 4h: commodity avg `-0.5981` n `12`; crypto_alt avg `2.4941` n `228`; crypto_major avg `2.885` n `8`; equity avg `0.6522` n `74`; fx avg `-0.0545` n `6`; index avg `0.2655` n `23`; metal avg `0.3926` n `18`; unknown avg `1.2381` n `516`
- 24h: commodity avg `-0.0385` n `12`; crypto_alt avg `2.8918` n `228`; crypto_major avg `4.8658` n `8`; equity avg `1.218` n `74`; fx avg `-0.0629` n `6`; index avg `0.3279` n `23`; metal avg `0.6747` n `18`; unknown avg `-4.5698` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
