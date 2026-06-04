# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T03:37:22.945268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0946` n `12`; crypto_alt avg `0.2056` n `228`; crypto_major avg `0.4276` n `8`; equity avg `0.1822` n `73`; fx avg `0.0002` n `6`; index avg `0.0226` n `23`; metal avg `-0.0614` n `18`; unknown avg `0.6471` n `420`
- 1h: commodity avg `0.0196` n `12`; crypto_alt avg `1.9696` n `228`; crypto_major avg `1.628` n `8`; equity avg `0.5893` n `73`; fx avg `-0.0077` n `6`; index avg `0.1818` n `23`; metal avg `0.1584` n `18`; unknown avg `1.158` n `420`
- 4h: commodity avg `-0.3322` n `12`; crypto_alt avg `-2.2603` n `228`; crypto_major avg `-0.5159` n `8`; equity avg `0.767` n `73`; fx avg `-0.0192` n `6`; index avg `0.08` n `23`; metal avg `0.2034` n `18`; unknown avg `-0.5013` n `419`
- 24h: commodity avg `0.0497` n `12`; crypto_alt avg `-0.4284` n `228`; crypto_major avg `-0.7466` n `8`; equity avg `-3.2853` n `73`; fx avg `-0.0061` n `6`; index avg `-1.1332` n `23`; metal avg `-1.7498` n `18`; unknown avg `0.7008` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
