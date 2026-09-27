# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T03:07:24.977147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.0443` n `234`; crypto_major avg `0.0244` n `8`; equity avg `0.0122` n `141`; fx avg `0.0` n `6`; index avg `0.0013` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.1201` n `959`
- 1h: commodity avg `0.0508` n `12`; crypto_alt avg `-0.234` n `234`; crypto_major avg `-0.0609` n `8`; equity avg `0.049` n `141`; fx avg `-0.0114` n `6`; index avg `0.0053` n `26`; metal avg `-0.0005` n `20`; unknown avg `1.149` n `955`
- 4h: commodity avg `-0.0864` n `12`; crypto_alt avg `-0.1127` n `234`; crypto_major avg `0.1896` n `8`; equity avg `0.0949` n `141`; fx avg `-0.0059` n `6`; index avg `0.0066` n `26`; metal avg `0.0019` n `20`; unknown avg `2.056` n `947`
- 24h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.8258` n `234`; crypto_major avg `-0.3467` n `8`; equity avg `0.2414` n `141`; fx avg `0.0095` n `6`; index avg `-0.0356` n `26`; metal avg `-0.0094` n `20`; unknown avg `4.5072` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
