# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T04:08:46.263047+00:00`
- Correlation status: `ready`
- Asset price records: `231`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4658` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4234` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.183` n `7`; crypto_alt avg `0.4284` n `223`; crypto_major avg `0.3968` n `7`; equity avg `0.0827` n `42`; fx avg `0.007` n `4`; index avg `0.0847` n `9`; metal avg `-0.0346` n `7`; unknown avg `0.0076` n `314`
- 1h: commodity avg `-0.1153` n `7`; crypto_alt avg `0.2393` n `223`; crypto_major avg `0.2459` n `7`; equity avg `0.0375` n `42`; fx avg `-0.0632` n `4`; index avg `0.0702` n `9`; metal avg `0.0023` n `7`; unknown avg `-0.0403` n `314`
- 4h: commodity avg `-0.0946` n `7`; crypto_alt avg `2.2483` n `223`; crypto_major avg `2.3712` n `7`; equity avg `1.2288` n `42`; fx avg `-0.0286` n `4`; index avg `0.6288` n `9`; metal avg `-0.0522` n `7`; unknown avg `0.37` n `314`
- 24h: commodity avg `-0.0381` n `7`; crypto_alt avg `2.9224` n `223`; crypto_major avg `2.9233` n `7`; equity avg `1.273` n `42`; fx avg `-0.05` n `4`; index avg `0.8474` n `9`; metal avg `0.3095` n `7`; unknown avg `0.7666` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3986`, n `223`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3885`, n `223`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.366`, n `227`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3504`, n `227`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2155`, n `223`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1993`, n `223`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1946`, n `227`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.188`, n `227`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1824`, n `227`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1419`, n `223`, weak_sample_signal
