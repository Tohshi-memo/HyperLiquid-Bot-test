# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T10:37:28.897788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.0688` n `230`; crypto_major avg `-0.1166` n `8`; equity avg `0.1131` n `102`; fx avg `0.0002` n `6`; index avg `0.0159` n `25`; metal avg `-0.0332` n `20`; unknown avg `-0.0238` n `785`
- 1h: commodity avg `-0.0438` n `12`; crypto_alt avg `0.0192` n `230`; crypto_major avg `0.0859` n `8`; equity avg `-0.5324` n `102`; fx avg `-0.0305` n `6`; index avg `-0.0678` n `25`; metal avg `-0.0531` n `20`; unknown avg `0.0074` n `784`
- 4h: commodity avg `0.0672` n `12`; crypto_alt avg `0.0719` n `230`; crypto_major avg `0.0728` n `8`; equity avg `-1.2831` n `102`; fx avg `-0.0429` n `6`; index avg `-0.1445` n `25`; metal avg `-0.1849` n `20`; unknown avg `-0.0101` n `784`
- 24h: commodity avg `-0.3185` n `12`; crypto_alt avg `-0.7463` n `230`; crypto_major avg `-0.2216` n `8`; equity avg `-0.6737` n `102`; fx avg `-0.1888` n `6`; index avg `-0.149` n `25`; metal avg `-0.2067` n `20`; unknown avg `1.0497` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
