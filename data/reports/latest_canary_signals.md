# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T05:52:31.164218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `0.0435` n `234`; crypto_major avg `0.0177` n `8`; equity avg `0.0135` n `141`; fx avg `0.0001` n `6`; index avg `-0.0002` n `26`; metal avg `0.001` n `20`; unknown avg `-0.2026` n `961`
- 1h: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.1007` n `234`; crypto_major avg `-0.2191` n `8`; equity avg `0.0116` n `141`; fx avg `-0.0042` n `6`; index avg `-0.0003` n `26`; metal avg `0.0024` n `20`; unknown avg `-0.2494` n `959`
- 4h: commodity avg `-0.0497` n `12`; crypto_alt avg `-0.2463` n `234`; crypto_major avg `-0.7552` n `8`; equity avg `0.0108` n `141`; fx avg `-0.0023` n `6`; index avg `0.0097` n `26`; metal avg `-0.0063` n `20`; unknown avg `14.7486` n `952`
- 24h: commodity avg `0.0822` n `12`; crypto_alt avg `3.007` n `234`; crypto_major avg `0.8528` n `8`; equity avg `-0.5562` n `141`; fx avg `-0.1011` n `6`; index avg `0.0724` n `26`; metal avg `0.219` n `20`; unknown avg `1126.9585` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
