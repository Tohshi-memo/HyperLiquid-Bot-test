# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T02:07:28.644473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `13`; crypto_alt avg `0.0346` n `239`; crypto_major avg `-0.0381` n `8`; equity avg `-0.0149` n `158`; fx avg `-0.0011` n `6`; index avg `-0.0043` n `27`; metal avg `-0.0034` n `20`; unknown avg `-0.1542` n `1258`
- 1h: commodity avg `0.0193` n `13`; crypto_alt avg `-0.3903` n `239`; crypto_major avg `-0.1582` n `8`; equity avg `-0.0587` n `158`; fx avg `0.0203` n `6`; index avg `-0.0107` n `27`; metal avg `-0.0122` n `20`; unknown avg `-0.0138` n `1254`
- 4h: commodity avg `-0.0444` n `13`; crypto_alt avg `-0.1734` n `239`; crypto_major avg `0.0536` n `8`; equity avg `0.0315` n `158`; fx avg `0.0228` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0116` n `20`; unknown avg `-0.2533` n `1232`
- 24h: commodity avg `0.0834` n `13`; crypto_alt avg `-2.0482` n `239`; crypto_major avg `-1.0808` n `8`; equity avg `-0.2676` n `158`; fx avg `0.0082` n `6`; index avg `0.0354` n `27`; metal avg `-0.052` n `20`; unknown avg `160.8375` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
