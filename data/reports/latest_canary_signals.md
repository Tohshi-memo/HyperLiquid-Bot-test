# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T05:22:24.855935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6842` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.1582` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `-0.0437` n `228`; crypto_major avg `-0.2864` n `8`; equity avg `0.0284` n `74`; fx avg `-0.0084` n `6`; index avg `-0.0045` n `23`; metal avg `-0.1185` n `18`; unknown avg `0.0553` n `424`
- 1h: commodity avg `0.0427` n `12`; crypto_alt avg `0.5742` n `228`; crypto_major avg `0.3124` n `8`; equity avg `0.3321` n `74`; fx avg `-0.0338` n `6`; index avg `0.153` n `23`; metal avg `0.0149` n `18`; unknown avg `0.3389` n `424`
- 4h: commodity avg `0.1351` n `12`; crypto_alt avg `-0.8451` n `228`; crypto_major avg `-0.9663` n `8`; equity avg `0.7179` n `74`; fx avg `-0.0346` n `6`; index avg `0.1919` n `23`; metal avg `0.0098` n `18`; unknown avg `-0.0919` n `424`
- 24h: commodity avg `-0.2124` n `12`; crypto_alt avg `-3.721` n `228`; crypto_major avg `-3.6104` n `8`; equity avg `-1.1215` n `73`; fx avg `0.1684` n `6`; index avg `-0.413` n `23`; metal avg `-0.5869` n `18`; unknown avg `-0.4468` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
