# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T11:37:30.615673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `0.0196` n `230`; crypto_major avg `0.039` n `8`; equity avg `0.0028` n `113`; fx avg `0.0024` n `6`; index avg `0.0005` n `25`; metal avg `0.0721` n `20`; unknown avg `-0.0278` n `787`
- 1h: commodity avg `-0.0384` n `12`; crypto_alt avg `-0.0007` n `230`; crypto_major avg `-0.0101` n `8`; equity avg `0.1913` n `113`; fx avg `0.0095` n `6`; index avg `0.0224` n `25`; metal avg `0.1138` n `20`; unknown avg `2.3171` n `787`
- 4h: commodity avg `-0.2484` n `12`; crypto_alt avg `0.0154` n `230`; crypto_major avg `-0.1232` n `8`; equity avg `0.6129` n `113`; fx avg `-0.0203` n `6`; index avg `0.0849` n `25`; metal avg `0.1628` n `20`; unknown avg `1.4326` n `787`
- 24h: commodity avg `-0.1202` n `12`; crypto_alt avg `-0.549` n `230`; crypto_major avg `-0.4257` n `8`; equity avg `1.8106` n `113`; fx avg `-0.0315` n `6`; index avg `0.3511` n `25`; metal avg `-0.112` n `20`; unknown avg `0.8329` n `755`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
