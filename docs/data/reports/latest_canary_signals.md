# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T18:53:19.226468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7695` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4195` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0573` n `12`; crypto_alt avg `-0.1224` n `231`; crypto_major avg `-0.0384` n `8`; equity avg `-0.0222` n `122`; fx avg `-0.0011` n `6`; index avg `-0.025` n `25`; metal avg `0.0406` n `20`; unknown avg `0.0088` n `794`
- 1h: commodity avg `0.1041` n `12`; crypto_alt avg `0.2485` n `231`; crypto_major avg `0.1694` n `8`; equity avg `0.3563` n `122`; fx avg `0.0043` n `6`; index avg `0.0805` n `25`; metal avg `0.0301` n `20`; unknown avg `-0.0767` n `794`
- 4h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.9332` n `231`; crypto_major avg `-1.3398` n `8`; equity avg `0.4297` n `122`; fx avg `-0.0416` n `6`; index avg `0.0797` n `25`; metal avg `-0.1765` n `20`; unknown avg `-0.0908` n `793`
- 24h: commodity avg `-0.1199` n `12`; crypto_alt avg `-1.5869` n `231`; crypto_major avg `-0.8132` n `8`; equity avg `-2.3926` n `122`; fx avg `-0.1508` n `6`; index avg `-0.3081` n `25`; metal avg `0.0313` n `20`; unknown avg `2.5511` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
