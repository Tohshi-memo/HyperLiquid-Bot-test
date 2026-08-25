# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T10:18:37.058153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.0626` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6992` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0319` n `12`; crypto_alt avg `-0.01` n `231`; crypto_major avg `0.0214` n `8`; equity avg `-0.0126` n `122`; fx avg `-0.0039` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.0048` n `795`
- 1h: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.5095` n `231`; crypto_major avg `-0.6642` n `8`; equity avg `0.2127` n `122`; fx avg `-0.0186` n `6`; index avg `0.0304` n `25`; metal avg `0.0266` n `20`; unknown avg `-0.1231` n `794`
- 4h: commodity avg `-0.3226` n `12`; crypto_alt avg `-1.5364` n `231`; crypto_major avg `-1.5981` n `8`; equity avg `0.4645` n `122`; fx avg `0.0097` n `6`; index avg `0.1011` n `25`; metal avg `-0.1284` n `20`; unknown avg `-0.2401` n `794`
- 24h: commodity avg `-0.6104` n `12`; crypto_alt avg `0.1267` n `231`; crypto_major avg `1.0412` n `8`; equity avg `0.7228` n `122`; fx avg `0.0361` n `6`; index avg `0.1296` n `25`; metal avg `-0.2318` n `20`; unknown avg `0.0683` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
