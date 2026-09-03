# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T15:52:29.636839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.2701` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.1334` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2851` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0584` n `12`; crypto_alt avg `0.3577` n `232`; crypto_major avg `0.6181` n `8`; equity avg `0.1138` n `133`; fx avg `-0.0067` n `6`; index avg `0.0138` n `26`; metal avg `-0.0838` n `20`; unknown avg `1.3744` n `792`
- 1h: commodity avg `-0.2759` n `12`; crypto_alt avg `1.0551` n `232`; crypto_major avg `1.2673` n `8`; equity avg `1.0275` n `133`; fx avg `-0.0014` n `6`; index avg `0.1984` n `26`; metal avg `0.2128` n `20`; unknown avg `1.7836` n `790`
- 4h: commodity avg `-0.5429` n `12`; crypto_alt avg `2.2367` n `232`; crypto_major avg `3.7272` n `8`; equity avg `1.4421` n `133`; fx avg `-0.0236` n `6`; index avg `0.3095` n `26`; metal avg `0.5938` n `20`; unknown avg `23.8182` n `790`
- 24h: commodity avg `-0.1279` n `12`; crypto_alt avg `4.3385` n `232`; crypto_major avg `5.4678` n `8`; equity avg `2.069` n `133`; fx avg `-0.3036` n `6`; index avg `0.2077` n `26`; metal avg `0.9221` n `20`; unknown avg `0.6841` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
