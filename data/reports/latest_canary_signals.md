# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T06:34:33.704417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `13`; crypto_alt avg `0.0559` n `239`; crypto_major avg `-0.0059` n `8`; equity avg `-0.0051` n `158`; fx avg `-0.0005` n `6`; index avg `-0.0021` n `27`; metal avg `-0.004` n `20`; unknown avg `0.0006` n `1259`
- 1h: commodity avg `-0.02` n `13`; crypto_alt avg `-0.0849` n `239`; crypto_major avg `0.0559` n `8`; equity avg `-0.0855` n `158`; fx avg `-0.0178` n `6`; index avg `-0.003` n `27`; metal avg `-0.0146` n `20`; unknown avg `-0.0992` n `1227`
- 4h: commodity avg `-0.074` n `13`; crypto_alt avg `-0.2407` n `239`; crypto_major avg `-0.1921` n `8`; equity avg `-0.0918` n `158`; fx avg `-0.0235` n `6`; index avg `0.0037` n `27`; metal avg `-0.0113` n `20`; unknown avg `-0.0048` n `1205`
- 24h: commodity avg `-0.3722` n `13`; crypto_alt avg `0.0446` n `239`; crypto_major avg `0.1257` n `8`; equity avg `1.2051` n `158`; fx avg `-0.0494` n `6`; index avg `0.2021` n `27`; metal avg `0.2136` n `20`; unknown avg `8.3746` n `1008`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
