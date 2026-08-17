# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T20:37:53.341712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0198` n `12`; crypto_alt avg `0.1316` n `230`; crypto_major avg `0.129` n `8`; equity avg `-0.007` n `114`; fx avg `0.0073` n `6`; index avg `-0.0102` n `25`; metal avg `-0.019` n `20`; unknown avg `-0.0455` n `792`
- 1h: commodity avg `0.0774` n `12`; crypto_alt avg `-0.0761` n `230`; crypto_major avg `-0.0117` n `8`; equity avg `-0.1611` n `114`; fx avg `0.0119` n `6`; index avg `-0.0222` n `25`; metal avg `-0.0122` n `20`; unknown avg `-0.0765` n `792`
- 4h: commodity avg `0.4314` n `12`; crypto_alt avg `-0.1547` n `230`; crypto_major avg `-0.2045` n `8`; equity avg `-0.647` n `114`; fx avg `-0.0007` n `6`; index avg `-0.1384` n `25`; metal avg `-0.1111` n `20`; unknown avg `0.0297` n `792`
- 24h: commodity avg `0.3784` n `12`; crypto_alt avg `-0.1234` n `230`; crypto_major avg `0.8428` n `8`; equity avg `0.9945` n `114`; fx avg `0.0214` n `6`; index avg `0.0424` n `25`; metal avg `0.2062` n `20`; unknown avg `0.1944` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
