# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T14:37:33.709822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0547` n `13`; crypto_alt avg `0.2358` n `239`; crypto_major avg `0.2004` n `8`; equity avg `0.0471` n `158`; fx avg `-0.0011` n `6`; index avg `-0.0078` n `27`; metal avg `-0.0044` n `20`; unknown avg `-0.2386` n `1254`
- 1h: commodity avg `-0.0451` n `13`; crypto_alt avg `-0.0811` n `239`; crypto_major avg `-0.0479` n `8`; equity avg `-0.0284` n `158`; fx avg `-0.0097` n `6`; index avg `-0.0105` n `27`; metal avg `-0.0059` n `20`; unknown avg `0.8339` n `1248`
- 4h: commodity avg `-0.0634` n `13`; crypto_alt avg `-0.252` n `239`; crypto_major avg `0.3215` n `8`; equity avg `0.1002` n `158`; fx avg `-0.0078` n `6`; index avg `-0.0135` n `27`; metal avg `-0.0056` n `20`; unknown avg `1.0465` n `1242`
- 24h: commodity avg `0.0494` n `13`; crypto_alt avg `-1.7622` n `239`; crypto_major avg `-0.3087` n `8`; equity avg `0.1901` n `158`; fx avg `0.0252` n `6`; index avg `-0.0021` n `27`; metal avg `-0.0427` n `20`; unknown avg `7.8952` n `1091`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
