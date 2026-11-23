# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T22:37:28.155749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8578` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5373` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0003` n `13`; crypto_alt avg `-0.3658` n `239`; crypto_major avg `-0.4492` n `8`; equity avg `0.1389` n `166`; fx avg `0.0139` n `6`; index avg `0.0245` n `27`; metal avg `-0.004` n `20`; unknown avg `1.2025` n `1266`
- 1h: commodity avg `0.016` n `13`; crypto_alt avg `-0.9122` n `239`; crypto_major avg `-0.6083` n `8`; equity avg `0.3839` n `166`; fx avg `0.0148` n `6`; index avg `0.0548` n `27`; metal avg `0.0208` n `20`; unknown avg `364.7137` n `1260`
- 4h: commodity avg `-0.1633` n `13`; crypto_alt avg `-2.1198` n `239`; crypto_major avg `-1.4795` n `8`; equity avg `0.3783` n `166`; fx avg `0.0119` n `6`; index avg `0.0578` n `27`; metal avg `-0.0673` n `20`; unknown avg `1.1457` n `1220`
- 24h: commodity avg `-1.4053` n `13`; crypto_alt avg `0.6006` n `239`; crypto_major avg `1.1555` n `8`; equity avg `6.6384` n `166`; fx avg `-0.1534` n `6`; index avg `0.6734` n `27`; metal avg `0.6335` n `20`; unknown avg `99.2493` n `1050`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
