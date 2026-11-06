# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T22:37:34.398384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.0272` n `239`; crypto_major avg `0.0254` n `8`; equity avg `0.0084` n `158`; fx avg `-0.0015` n `6`; index avg `-0.0217` n `27`; metal avg `-0.0114` n `20`; unknown avg `-0.0948` n `1261`
- 1h: commodity avg `0.0589` n `13`; crypto_alt avg `-0.0532` n `239`; crypto_major avg `0.3622` n `8`; equity avg `0.1207` n `158`; fx avg `-0.009` n `6`; index avg `-0.0169` n `27`; metal avg `0.0421` n `20`; unknown avg `0.0448` n `1247`
- 4h: commodity avg `0.141` n `13`; crypto_alt avg `-0.4` n `239`; crypto_major avg `-0.0109` n `8`; equity avg `0.5413` n `158`; fx avg `0.0165` n `6`; index avg `-0.0164` n `27`; metal avg `0.0124` n `20`; unknown avg `-0.0513` n `1181`
- 24h: commodity avg `0.0042` n `13`; crypto_alt avg `1.7486` n `239`; crypto_major avg `0.2117` n `8`; equity avg `3.0869` n `158`; fx avg `-0.074` n `6`; index avg `0.4044` n `27`; metal avg `0.0562` n `20`; unknown avg `0.4134` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
