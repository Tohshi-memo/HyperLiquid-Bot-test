# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T04:22:23.187045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.045` n `12`; crypto_alt avg `-0.0308` n `228`; crypto_major avg `0.2229` n `8`; equity avg `0.0514` n `73`; fx avg `0.0045` n `6`; index avg `0.0102` n `23`; metal avg `0.1936` n `18`; unknown avg `-0.7302` n `420`
- 1h: commodity avg `0.1759` n `12`; crypto_alt avg `0.3601` n `228`; crypto_major avg `1.0068` n `8`; equity avg `0.2439` n `73`; fx avg `0.0122` n `6`; index avg `0.0293` n `23`; metal avg `0.1359` n `18`; unknown avg `0.3959` n `420`
- 4h: commodity avg `-0.2483` n `12`; crypto_alt avg `-2.3631` n `228`; crypto_major avg `0.0137` n `8`; equity avg `0.4851` n `73`; fx avg `0.0583` n `6`; index avg `0.0726` n `23`; metal avg `0.4389` n `18`; unknown avg `-0.6226` n `419`
- 24h: commodity avg `0.0131` n `12`; crypto_alt avg `-0.6644` n `228`; crypto_major avg `-0.7462` n `8`; equity avg `-3.3916` n `73`; fx avg `-0.0012` n `6`; index avg `-1.1147` n `23`; metal avg `-1.5224` n `18`; unknown avg `0.9538` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
