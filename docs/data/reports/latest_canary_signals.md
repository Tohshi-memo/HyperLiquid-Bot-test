# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T03:15:20.545648+00:00`
- Correlation status: `ready`
- Asset price records: `228`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6227` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.002` n `7`; crypto_alt avg `0.0347` n `223`; crypto_major avg `0.2023` n `7`; equity avg `0.0588` n `42`; fx avg `0.0122` n `4`; index avg `0.0981` n `9`; metal avg `0.0895` n `7`; unknown avg `-0.1543` n `314`
- 1h: commodity avg `0.09` n `7`; crypto_alt avg `0.7191` n `223`; crypto_major avg `0.6707` n `7`; equity avg `0.362` n `42`; fx avg `0.0172` n `4`; index avg `0.3222` n `9`; metal avg `0.16` n `7`; unknown avg `-0.2494` n `314`
- 4h: commodity avg `0.242` n `7`; crypto_alt avg `1.532` n `223`; crypto_major avg `1.6428` n `7`; equity avg `1.1646` n `42`; fx avg `0.0523` n `4`; index avg `0.8122` n `9`; metal avg `0.0201` n `7`; unknown avg `0.0656` n `314`
- 24h: commodity avg `0.0965` n `7`; crypto_alt avg `2.8622` n `223`; crypto_major avg `2.9745` n `7`; equity avg `1.3303` n `42`; fx avg `0.0268` n `4`; index avg `0.8782` n `9`; metal avg `0.3946` n `7`; unknown avg `0.5916` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3865`, n `220`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3773`, n `220`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3718`, n `224`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3562`, n `224`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2118`, n `220`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1997`, n `220`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1932`, n `224`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1893`, n `224`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1836`, n `224`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1407`, n `224`, weak_sample_signal
