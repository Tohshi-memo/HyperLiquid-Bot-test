# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T05:37:41.438248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0201` n `12`; crypto_alt avg `0.1027` n `231`; crypto_major avg `0.1211` n `8`; equity avg `0.0091` n `122`; fx avg `0.007` n `6`; index avg `0.0055` n `25`; metal avg `-0.0112` n `20`; unknown avg `-0.0016` n `794`
- 1h: commodity avg `-0.0391` n `12`; crypto_alt avg `0.5238` n `231`; crypto_major avg `0.5662` n `8`; equity avg `0.3964` n `122`; fx avg `0.0007` n `6`; index avg `0.0496` n `25`; metal avg `0.1072` n `20`; unknown avg `0.304` n `794`
- 4h: commodity avg `-0.067` n `12`; crypto_alt avg `1.1754` n `231`; crypto_major avg `1.0748` n `8`; equity avg `1.0289` n `122`; fx avg `0.0011` n `6`; index avg `0.1596` n `25`; metal avg `-0.3028` n `20`; unknown avg `1.1216` n `794`
- 24h: commodity avg `-0.048` n `12`; crypto_alt avg `2.2541` n `231`; crypto_major avg `3.2543` n `8`; equity avg `0.1893` n `122`; fx avg `0.0624` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0409` n `20`; unknown avg `0.634` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
