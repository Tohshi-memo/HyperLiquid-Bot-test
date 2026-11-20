# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T12:22:25.685589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.523` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3312` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `0.3097` n `239`; crypto_major avg `0.2948` n `8`; equity avg `0.1303` n `165`; fx avg `0.0192` n `6`; index avg `0.0087` n `27`; metal avg `0.0509` n `20`; unknown avg `3.4216` n `1260`
- 1h: commodity avg `0.0329` n `13`; crypto_alt avg `-0.624` n `239`; crypto_major avg `-0.7903` n `8`; equity avg `-0.4294` n `165`; fx avg `0.0178` n `6`; index avg `-0.0114` n `27`; metal avg `-0.0782` n `20`; unknown avg `159.7739` n `1252`
- 4h: commodity avg `0.0388` n `13`; crypto_alt avg `-1.2826` n `239`; crypto_major avg `-1.4992` n `8`; equity avg `-1.5941` n `165`; fx avg `0.02` n `6`; index avg `-0.168` n `27`; metal avg `0.0238` n `20`; unknown avg `29.4199` n `1240`
- 24h: commodity avg `-0.4119` n `13`; crypto_alt avg `-4.2383` n `239`; crypto_major avg `-4.0174` n `8`; equity avg `-8.3501` n `165`; fx avg `-0.046` n `6`; index avg `-0.839` n `27`; metal avg `-1.2315` n `20`; unknown avg `45.5887` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
