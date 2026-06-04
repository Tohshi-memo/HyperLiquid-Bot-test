# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T18:12:38.743042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.1611` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.8199` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `-0.7508` n `228`; crypto_major avg `-0.6158` n `8`; equity avg `-0.0627` n `74`; fx avg `-0.003` n `6`; index avg `0.0335` n `23`; metal avg `0.0025` n `18`; unknown avg `-0.2134` n `424`
- 1h: commodity avg `-0.041` n `12`; crypto_alt avg `-0.9808` n `228`; crypto_major avg `-0.7185` n `8`; equity avg `0.1581` n `74`; fx avg `-0.0125` n `6`; index avg `0.2332` n `23`; metal avg `-0.0368` n `18`; unknown avg `0.5174` n `424`
- 4h: commodity avg `-0.1373` n `12`; crypto_alt avg `-0.4948` n `228`; crypto_major avg `-1.0635` n `8`; equity avg `0.7564` n `74`; fx avg `-0.0387` n `6`; index avg `1.0976` n `23`; metal avg `-0.0627` n `18`; unknown avg `1.4241` n `424`
- 24h: commodity avg `-0.7716` n `12`; crypto_alt avg `-6.0662` n `228`; crypto_major avg `-4.625` n `8`; equity avg `-1.0868` n `73`; fx avg `0.0547` n `6`; index avg `0.0331` n `23`; metal avg `0.7446` n `18`; unknown avg `1.0445` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
