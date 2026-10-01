# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T06:11:19.072755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0534` n `13`; crypto_alt avg `0.0666` n `234`; crypto_major avg `0.0334` n `8`; equity avg `0.1396` n `142`; fx avg `-0.0209` n `6`; index avg `0.019` n `26`; metal avg `0.043` n `20`; unknown avg `-0.187` n `946`
- 1h: commodity avg `0.3789` n `13`; crypto_alt avg `0.1225` n `234`; crypto_major avg `0.2209` n `8`; equity avg `0.2672` n `142`; fx avg `0.0139` n `6`; index avg `0.0381` n `26`; metal avg `0.0661` n `20`; unknown avg `0.3523` n `946`
- 4h: commodity avg `-0.117` n `13`; crypto_alt avg `1.257` n `234`; crypto_major avg `0.7609` n `8`; equity avg `1.1177` n `142`; fx avg `-0.0264` n `6`; index avg `0.2311` n `26`; metal avg `0.2976` n `20`; unknown avg `1.2487` n `940`
- 24h: commodity avg `-0.2369` n `13`; crypto_alt avg `1.2329` n `234`; crypto_major avg `1.3596` n `8`; equity avg `1.2163` n `142`; fx avg `0.1314` n `6`; index avg `0.3114` n `26`; metal avg `0.0787` n `20`; unknown avg `773.8744` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
