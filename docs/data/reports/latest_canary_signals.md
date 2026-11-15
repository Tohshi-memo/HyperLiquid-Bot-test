# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T00:22:25.152300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.704` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.518` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `0.4443` n `239`; crypto_major avg `0.5853` n `8`; equity avg `0.0073` n `162`; fx avg `0.0008` n `6`; index avg `0.0001` n `27`; metal avg `0.003` n `20`; unknown avg `0.0726` n `1260`
- 1h: commodity avg `0.0123` n `13`; crypto_alt avg `1.4889` n `239`; crypto_major avg `1.204` n `8`; equity avg `0.2843` n `162`; fx avg `-0.0072` n `6`; index avg `0.0159` n `27`; metal avg `-0.0002` n `20`; unknown avg `0.8429` n `1252`
- 4h: commodity avg `0.0992` n `13`; crypto_alt avg `-0.6857` n `239`; crypto_major avg `-1.6991` n `8`; equity avg `-0.2339` n `162`; fx avg `0.0134` n `6`; index avg `0.0049` n `27`; metal avg `-0.1811` n `20`; unknown avg `41.9995` n `1188`
- 24h: commodity avg `0.0207` n `13`; crypto_alt avg `-7.8839` n `239`; crypto_major avg `-7.8128` n `8`; equity avg `-1.4189` n `162`; fx avg `0.0174` n `6`; index avg `-0.1054` n `27`; metal avg `-0.4407` n `20`; unknown avg `46.8303` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
