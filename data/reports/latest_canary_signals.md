# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T19:07:33.873314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.64` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.1464` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5411` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0641` n `12`; crypto_alt avg `0.4573` n `234`; crypto_major avg `0.4178` n `8`; equity avg `-0.4214` n `137`; fx avg `0.0181` n `6`; index avg `-0.1064` n `27`; metal avg `-0.1202` n `20`; unknown avg `0.5288` n `887`
- 1h: commodity avg `0.0633` n `12`; crypto_alt avg `-0.1967` n `234`; crypto_major avg `-0.2192` n `8`; equity avg `-1.3369` n `137`; fx avg `0.0392` n `6`; index avg `-0.2827` n `27`; metal avg `-0.5085` n `20`; unknown avg `10.6085` n `881`
- 4h: commodity avg `0.0539` n `12`; crypto_alt avg `1.0169` n `234`; crypto_major avg `0.9024` n `8`; equity avg `-1.244` n `137`; fx avg `0.0041` n `6`; index avg `-0.2996` n `27`; metal avg `-0.6387` n `20`; unknown avg `0.633` n `875`
- 24h: commodity avg `-0.5234` n `12`; crypto_alt avg `-0.7653` n `234`; crypto_major avg `0.1016` n `8`; equity avg `0.2858` n `137`; fx avg `0.0257` n `6`; index avg `-0.012` n `27`; metal avg `-0.3659` n `20`; unknown avg `5.1198` n `799`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
