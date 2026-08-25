# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T09:07:32.960426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6804` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2569` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0669` n `12`; crypto_alt avg `0.0428` n `231`; crypto_major avg `0.0791` n `8`; equity avg `0.1956` n `122`; fx avg `-0.0093` n `6`; index avg `0.05` n `25`; metal avg `-0.017` n `20`; unknown avg `0.0064` n `794`
- 1h: commodity avg `-0.3439` n `12`; crypto_alt avg `0.1276` n `231`; crypto_major avg `0.0537` n `8`; equity avg `0.4925` n `122`; fx avg `-0.0089` n `6`; index avg `0.0959` n `25`; metal avg `-0.0662` n `20`; unknown avg `-0.0154` n `794`
- 4h: commodity avg `-0.4309` n `12`; crypto_alt avg `-1.2526` n `231`; crypto_major avg `-1.1162` n `8`; equity avg `0.5642` n `122`; fx avg `0.0641` n `6`; index avg `0.1407` n `25`; metal avg `-0.1443` n `20`; unknown avg `-0.3079` n `778`
- 24h: commodity avg `-0.4798` n `12`; crypto_alt avg `0.8203` n `231`; crypto_major avg `2.0358` n `8`; equity avg `0.3944` n `122`; fx avg `0.0482` n `6`; index avg `0.0878` n `25`; metal avg `-0.2797` n `20`; unknown avg `0.0502` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
