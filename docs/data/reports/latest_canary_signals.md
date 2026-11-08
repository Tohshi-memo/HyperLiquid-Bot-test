# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T06:37:28.049816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0407` n `13`; crypto_alt avg `-0.1997` n `239`; crypto_major avg `-0.0761` n `8`; equity avg `-0.028` n `158`; fx avg `-0.0006` n `6`; index avg `-0.0061` n `27`; metal avg `0.0116` n `20`; unknown avg `-0.0523` n `1260`
- 1h: commodity avg `0.0212` n `13`; crypto_alt avg `-0.0674` n `239`; crypto_major avg `-0.0189` n `8`; equity avg `-0.0011` n `158`; fx avg `0.007` n `6`; index avg `0.0003` n `27`; metal avg `0.0042` n `20`; unknown avg `-0.0145` n `1226`
- 4h: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.1105` n `239`; crypto_major avg `0.1296` n `8`; equity avg `0.0895` n `158`; fx avg `0.0192` n `6`; index avg `0.0025` n `27`; metal avg `0.0039` n `20`; unknown avg `-0.1186` n `1210`
- 24h: commodity avg `0.1693` n `13`; crypto_alt avg `-1.7959` n `239`; crypto_major avg `-0.6796` n `8`; equity avg `0.0164` n `158`; fx avg `0.0386` n `6`; index avg `0.0308` n `27`; metal avg `-0.0375` n `20`; unknown avg `158.7852` n `1081`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
