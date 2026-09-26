# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T06:07:31.143862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.0769` n `234`; crypto_major avg `-0.0523` n `8`; equity avg `-0.0104` n `141`; fx avg `-0.0064` n `6`; index avg `0.0` n `26`; metal avg `-0.0004` n `20`; unknown avg `-0.0898` n `935`
- 1h: commodity avg `0.0073` n `12`; crypto_alt avg `-0.0539` n `234`; crypto_major avg `-0.1905` n `8`; equity avg `-0.0538` n `141`; fx avg `-0.0105` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0002` n `20`; unknown avg `-0.1836` n `935`
- 4h: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.2059` n `234`; crypto_major avg `-0.7687` n `8`; equity avg `-0.0095` n `141`; fx avg `-0.0073` n `6`; index avg `0.0023` n `26`; metal avg `-0.0107` n `20`; unknown avg `-0.2776` n `928`
- 24h: commodity avg `0.13` n `12`; crypto_alt avg `3.0112` n `234`; crypto_major avg `0.779` n `8`; equity avg `-0.6083` n `141`; fx avg `-0.124` n `6`; index avg `0.0718` n `26`; metal avg `0.2398` n `20`; unknown avg `1126.8729` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
