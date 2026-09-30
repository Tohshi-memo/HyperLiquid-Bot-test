# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T13:22:32.212542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.87` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `2.0594` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5544` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1774` n `12`; crypto_alt avg `0.0503` n `234`; crypto_major avg `-0.0053` n `8`; equity avg `-0.1188` n `142`; fx avg `0.0207` n `6`; index avg `-0.0582` n `26`; metal avg `-0.1263` n `20`; unknown avg `0.7062` n `963`
- 1h: commodity avg `0.1481` n `12`; crypto_alt avg `1.5335` n `234`; crypto_major avg `1.3394` n `8`; equity avg `0.6987` n `142`; fx avg `-0.0207` n `6`; index avg `0.116` n `26`; metal avg `0.0608` n `20`; unknown avg `6.8383` n `961`
- 4h: commodity avg `0.13` n `12`; crypto_alt avg `1.7163` n `234`; crypto_major avg `2.0209` n `8`; equity avg `0.4665` n `142`; fx avg `0.0237` n `6`; index avg `0.0525` n `26`; metal avg `-0.0385` n `20`; unknown avg `2.6532` n `955`
- 24h: commodity avg `0.1769` n `12`; crypto_alt avg `0.7718` n `234`; crypto_major avg `0.2605` n `8`; equity avg `0.2819` n `142`; fx avg `0.0175` n `6`; index avg `0.0641` n `26`; metal avg `0.1284` n `20`; unknown avg `2929.5939` n `826`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
