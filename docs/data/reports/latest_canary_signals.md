# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T18:37:38.388329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0685` n `12`; crypto_alt avg `-0.1297` n `230`; crypto_major avg `-0.0916` n `8`; equity avg `-0.0558` n `102`; fx avg `0.0001` n `6`; index avg `-0.0485` n `25`; metal avg `0.0216` n `20`; unknown avg `-0.0164` n `779`
- 1h: commodity avg `-0.0794` n `12`; crypto_alt avg `-0.093` n `230`; crypto_major avg `-0.0059` n `8`; equity avg `-0.1215` n `102`; fx avg `-0.0136` n `6`; index avg `0.0035` n `25`; metal avg `0.0401` n `20`; unknown avg `-0.014` n `779`
- 4h: commodity avg `-0.0667` n `12`; crypto_alt avg `-0.3298` n `230`; crypto_major avg `0.3011` n `8`; equity avg `-0.2334` n `102`; fx avg `-0.0214` n `6`; index avg `-0.0045` n `25`; metal avg `0.1941` n `20`; unknown avg `-0.1042` n `779`
- 24h: commodity avg `-0.1719` n `12`; crypto_alt avg `0.2988` n `230`; crypto_major avg `1.0398` n `8`; equity avg `3.7349` n `102`; fx avg `-0.3847` n `6`; index avg `0.2614` n `25`; metal avg `0.5445` n `20`; unknown avg `-0.078` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
