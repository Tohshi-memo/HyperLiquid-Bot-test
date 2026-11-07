# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T15:22:28.757598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `0.0984` n `239`; crypto_major avg `-0.0254` n `8`; equity avg `-0.0031` n `158`; fx avg `0.002` n `6`; index avg `-0.0` n `27`; metal avg `-0.0043` n `20`; unknown avg `0.0893` n `1261`
- 1h: commodity avg `-0.0077` n `13`; crypto_alt avg `-0.2124` n `239`; crypto_major avg `-0.1986` n `8`; equity avg `-0.0726` n `158`; fx avg `0.0059` n `6`; index avg `0.0001` n `27`; metal avg `-0.0095` n `20`; unknown avg `159.0732` n `1255`
- 4h: commodity avg `-0.0115` n `13`; crypto_alt avg `-0.0619` n `239`; crypto_major avg `-0.2172` n `8`; equity avg `-0.0516` n `158`; fx avg `0.0225` n `6`; index avg `0.0215` n `27`; metal avg `-0.006` n `20`; unknown avg `-0.098` n `1249`
- 24h: commodity avg `0.1972` n `13`; crypto_alt avg `-1.9766` n `239`; crypto_major avg `-0.7154` n `8`; equity avg `0.0281` n `158`; fx avg `-0.0009` n `6`; index avg `-0.0535` n `27`; metal avg `-0.0064` n `20`; unknown avg `-0.365` n `1121`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
