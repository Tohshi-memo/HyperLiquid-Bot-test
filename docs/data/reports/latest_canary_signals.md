# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T23:34:48.765954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `-0.0529` n `231`; crypto_major avg `-0.0163` n `8`; equity avg `-0.0615` n `122`; fx avg `-0.0061` n `6`; index avg `-0.0115` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.0645` n `795`
- 1h: commodity avg `0.0336` n `12`; crypto_alt avg `-0.2451` n `231`; crypto_major avg `-0.2314` n `8`; equity avg `-0.1092` n `122`; fx avg `-0.0039` n `6`; index avg `-0.0298` n `25`; metal avg `-0.0574` n `20`; unknown avg `-0.1279` n `795`
- 4h: commodity avg `-0.1864` n `12`; crypto_alt avg `-0.7474` n `231`; crypto_major avg `-0.7678` n `8`; equity avg `0.1293` n `122`; fx avg `0.0033` n `6`; index avg `0.0164` n `25`; metal avg `-0.014` n `20`; unknown avg `-0.2312` n `795`
- 24h: commodity avg `-0.7001` n `12`; crypto_alt avg `-2.0512` n `231`; crypto_major avg `-1.2753` n `8`; equity avg `2.0773` n `122`; fx avg `0.0471` n `6`; index avg `0.246` n `25`; metal avg `-0.1883` n `20`; unknown avg `-0.5208` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
