# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T09:52:28.808342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0769` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.9064` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.3333` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0114` n `13`; crypto_alt avg `0.2259` n `239`; crypto_major avg `0.1066` n `8`; equity avg `0.0138` n `166`; fx avg `0.0049` n `6`; index avg `0.01` n `27`; metal avg `0.0077` n `20`; unknown avg `0.29` n `1262`
- 1h: commodity avg `-0.0055` n `13`; crypto_alt avg `0.8648` n `239`; crypto_major avg `0.3198` n `8`; equity avg `-0.0295` n `166`; fx avg `-0.0234` n `6`; index avg `0.0094` n `27`; metal avg `0.0139` n `20`; unknown avg `200.245` n `1256`
- 4h: commodity avg `-0.0316` n `13`; crypto_alt avg `2.11` n `239`; crypto_major avg `3.0453` n `8`; equity avg `0.712` n `166`; fx avg `-0.0714` n `6`; index avg `0.075` n `27`; metal avg `0.1389` n `20`; unknown avg `207.5728` n `1208`
- 24h: commodity avg `0.8406` n `13`; crypto_alt avg `-5.2762` n `239`; crypto_major avg `-6.1763` n `8`; equity avg `-4.129` n `166`; fx avg `-0.1184` n `6`; index avg `-0.4552` n `27`; metal avg `-0.3158` n `20`; unknown avg `8.6571` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
