# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T10:07:30.065611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0259` n `13`; crypto_alt avg `-0.0098` n `239`; crypto_major avg `0.0433` n `8`; equity avg `-0.0198` n `158`; fx avg `0.0016` n `6`; index avg `-0.0135` n `27`; metal avg `0.0015` n `20`; unknown avg `1.6921` n `1257`
- 1h: commodity avg `0.027` n `13`; crypto_alt avg `-0.2726` n `239`; crypto_major avg `-0.1925` n `8`; equity avg `-0.247` n `158`; fx avg `0.0022` n `6`; index avg `-0.0352` n `27`; metal avg `-0.0032` n `20`; unknown avg `130.3791` n `1255`
- 4h: commodity avg `0.1015` n `13`; crypto_alt avg `-0.4717` n `239`; crypto_major avg `-0.079` n `8`; equity avg `0.0891` n `158`; fx avg `-0.0215` n `6`; index avg `0.0053` n `27`; metal avg `-0.0078` n `20`; unknown avg `136.823` n `1193`
- 24h: commodity avg `0.132` n `13`; crypto_alt avg `-0.8717` n `239`; crypto_major avg `-0.1845` n `8`; equity avg `-0.1067` n `158`; fx avg `0.0376` n `6`; index avg `0.0007` n `27`; metal avg `0.0441` n `20`; unknown avg `7.9087` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
