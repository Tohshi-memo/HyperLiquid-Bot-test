# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T16:22:38.812909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0477` n `12`; crypto_alt avg `-0.0771` n `230`; crypto_major avg `-0.0427` n `8`; equity avg `-0.2154` n `112`; fx avg `-0.0016` n `6`; index avg `-0.0161` n `25`; metal avg `-0.0444` n `20`; unknown avg `0.104` n `782`
- 1h: commodity avg `0.0428` n `12`; crypto_alt avg `0.1252` n `230`; crypto_major avg `0.0885` n `8`; equity avg `0.3118` n `112`; fx avg `-0.0302` n `6`; index avg `0.0065` n `25`; metal avg `-0.067` n `20`; unknown avg `0.0037` n `782`
- 4h: commodity avg `0.3568` n `12`; crypto_alt avg `-0.207` n `230`; crypto_major avg `-0.4047` n `8`; equity avg `0.4049` n `112`; fx avg `-0.0527` n `6`; index avg `0.0121` n `25`; metal avg `0.0386` n `20`; unknown avg `-0.0045` n `782`
- 24h: commodity avg `0.4198` n `12`; crypto_alt avg `-0.2401` n `230`; crypto_major avg `-0.0066` n `8`; equity avg `0.8864` n `112`; fx avg `-0.1364` n `6`; index avg `-0.0148` n `25`; metal avg `0.2967` n `20`; unknown avg `0.0575` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
