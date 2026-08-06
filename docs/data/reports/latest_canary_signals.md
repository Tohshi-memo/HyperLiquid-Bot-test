# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T07:07:27.488140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0404` n `12`; crypto_alt avg `-0.0024` n `230`; crypto_major avg `-0.0742` n `8`; equity avg `0.0941` n `108`; fx avg `-0.0263` n `6`; index avg `0.0254` n `25`; metal avg `0.0525` n `20`; unknown avg `0.0455` n `782`
- 1h: commodity avg `0.0524` n `12`; crypto_alt avg `0.1242` n `230`; crypto_major avg `-0.1548` n `8`; equity avg `-0.0019` n `108`; fx avg `0.0603` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0648` n `20`; unknown avg `0.0766` n `782`
- 4h: commodity avg `0.0041` n `12`; crypto_alt avg `0.5537` n `230`; crypto_major avg `0.3256` n `8`; equity avg `-0.1572` n `108`; fx avg `0.0652` n `6`; index avg `-0.0392` n `25`; metal avg `-0.1494` n `20`; unknown avg `0.0923` n `750`
- 24h: commodity avg `-0.0594` n `12`; crypto_alt avg `0.1634` n `230`; crypto_major avg `-0.1788` n `8`; equity avg `-2.1465` n `108`; fx avg `0.0073` n `6`; index avg `-0.3936` n `25`; metal avg `0.1358` n `20`; unknown avg `0.8444` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1922`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
