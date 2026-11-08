# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T03:52:26.429919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `0.0175` n `239`; crypto_major avg `0.0503` n `8`; equity avg `-0.024` n `158`; fx avg `-0.0037` n `6`; index avg `-0.0035` n `27`; metal avg `0.0063` n `20`; unknown avg `0.1492` n `1262`
- 1h: commodity avg `-0.0119` n `13`; crypto_alt avg `0.2874` n `239`; crypto_major avg `0.2862` n `8`; equity avg `0.0785` n `158`; fx avg `0.0069` n `6`; index avg `0.0044` n `27`; metal avg `0.0043` n `20`; unknown avg `6.1946` n `1256`
- 4h: commodity avg `0.0027` n `13`; crypto_alt avg `-0.6708` n `239`; crypto_major avg `-0.237` n `8`; equity avg `-0.0893` n `158`; fx avg `0.0378` n `6`; index avg `-0.0037` n `27`; metal avg `-0.0231` n `20`; unknown avg `-0.0505` n `1246`
- 24h: commodity avg `0.1433` n `13`; crypto_alt avg `-1.3727` n `239`; crypto_major avg `-0.4793` n `8`; equity avg `-0.144` n `158`; fx avg `0.0133` n `6`; index avg `0.0333` n `27`; metal avg `-0.046` n `20`; unknown avg `161.2565` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
