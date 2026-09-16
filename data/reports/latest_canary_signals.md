# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T18:52:31.045545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.73` - Polymarket crypto volume is unusually high.
- 1h_crypto_metal_divergence: score `1.5813` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.5795` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.037` n `12`; crypto_alt avg `0.8185` n `234`; crypto_major avg `0.6549` n `8`; equity avg `0.0226` n `137`; fx avg `-0.0095` n `6`; index avg `0.011` n `27`; metal avg `0.0266` n `20`; unknown avg `0.0429` n `917`
- 1h: commodity avg `0.0027` n `12`; crypto_alt avg `1.3775` n `234`; crypto_major avg `1.1938` n `8`; equity avg `-0.3857` n `137`; fx avg `-0.0067` n `6`; index avg `-0.1293` n `27`; metal avg `-0.3875` n `20`; unknown avg `11.0947` n `899`
- 4h: commodity avg `-0.1936` n `12`; crypto_alt avg `0.8166` n `234`; crypto_major avg `0.8286` n `8`; equity avg `-0.586` n `137`; fx avg `-0.0366` n `6`; index avg `-0.1364` n `27`; metal avg `-0.4919` n `20`; unknown avg `0.1318` n `893`
- 24h: commodity avg `-0.6189` n `12`; crypto_alt avg `-0.3952` n `234`; crypto_major avg `0.4172` n `8`; equity avg `0.952` n `137`; fx avg `0.0092` n `6`; index avg `0.1076` n `27`; metal avg `-0.261` n `20`; unknown avg `5.1232` n `799`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
