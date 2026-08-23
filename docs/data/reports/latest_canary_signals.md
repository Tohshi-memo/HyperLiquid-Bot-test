# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T16:52:29.420400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.2262` n `231`; crypto_major avg `0.0525` n `8`; equity avg `0.0413` n `122`; fx avg `0.0029` n `6`; index avg `0.0099` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.0471` n `793`
- 1h: commodity avg `-0.0062` n `12`; crypto_alt avg `0.0458` n `231`; crypto_major avg `0.1698` n `8`; equity avg `0.046` n `122`; fx avg `0.0026` n `6`; index avg `0.0095` n `25`; metal avg `0.0179` n `20`; unknown avg `-0.0406` n `793`
- 4h: commodity avg `-0.023` n `12`; crypto_alt avg `1.8002` n `231`; crypto_major avg `0.4749` n `8`; equity avg `0.1776` n `122`; fx avg `0.0034` n `6`; index avg `0.0264` n `25`; metal avg `0.0457` n `20`; unknown avg `1.0052` n `793`
- 24h: commodity avg `0.0244` n `12`; crypto_alt avg `2.0638` n `231`; crypto_major avg `0.9701` n `8`; equity avg `0.6967` n `122`; fx avg `0.0366` n `6`; index avg `0.0748` n `25`; metal avg `0.0903` n `20`; unknown avg `8.0129` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
