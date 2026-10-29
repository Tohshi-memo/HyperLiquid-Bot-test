# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T12:52:34.493719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.321` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0268` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5303` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1637` n `13`; crypto_alt avg `0.2433` n `238`; crypto_major avg `0.2466` n `8`; equity avg `0.2658` n `155`; fx avg `-0.014` n `6`; index avg `0.0088` n `27`; metal avg `-0.0155` n `20`; unknown avg `0.717` n `1239`
- 1h: commodity avg `-0.3646` n `13`; crypto_alt avg `0.3595` n `238`; crypto_major avg `0.255` n `8`; equity avg `0.0263` n `155`; fx avg `-0.0082` n `6`; index avg `-0.019` n `27`; metal avg `0.0198` n `20`; unknown avg `21.6798` n `1227`
- 4h: commodity avg `-0.357` n `13`; crypto_alt avg `1.6749` n `238`; crypto_major avg `1.964` n `8`; equity avg `0.4337` n `155`; fx avg `0.0421` n `6`; index avg `0.0612` n `27`; metal avg `-0.0628` n `20`; unknown avg `14.9845` n `1130`
- 24h: commodity avg `-0.6381` n `13`; crypto_alt avg `-0.46` n `238`; crypto_major avg `0.5927` n `8`; equity avg `-1.209` n `155`; fx avg `0.0327` n `6`; index avg `-0.0773` n `27`; metal avg `-0.6213` n `20`; unknown avg `16.2615` n `982`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
