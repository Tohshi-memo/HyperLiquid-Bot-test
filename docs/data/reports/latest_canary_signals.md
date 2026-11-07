# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T21:37:26.104572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `13`; crypto_alt avg `-0.0558` n `239`; crypto_major avg `0.014` n `8`; equity avg `0.0256` n `158`; fx avg `0.0033` n `6`; index avg `0.0094` n `27`; metal avg `0.0036` n `20`; unknown avg `-0.0427` n `1262`
- 1h: commodity avg `-0.0244` n `13`; crypto_alt avg `-0.7604` n `239`; crypto_major avg `-0.3354` n `8`; equity avg `-0.1772` n `158`; fx avg `0.0085` n `6`; index avg `-0.0122` n `27`; metal avg `-0.0068` n `20`; unknown avg `0.1062` n `1236`
- 4h: commodity avg `0.0099` n `13`; crypto_alt avg `-1.0069` n `239`; crypto_major avg `-0.5243` n `8`; equity avg `-0.1779` n `158`; fx avg `-0.0057` n `6`; index avg `-0.0078` n `27`; metal avg `-0.0114` n `20`; unknown avg `0.2005` n `1202`
- 24h: commodity avg `0.0993` n `13`; crypto_alt avg `-2.1248` n `239`; crypto_major avg `-0.8155` n `8`; equity avg `-0.1672` n `158`; fx avg `-0.0229` n `6`; index avg `0.0315` n `27`; metal avg `0.0108` n `20`; unknown avg `146.8268` n `1095`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
