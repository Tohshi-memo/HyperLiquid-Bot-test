# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T23:22:29.281366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `13`; crypto_alt avg `-0.06` n `239`; crypto_major avg `-0.05` n `8`; equity avg `-0.0288` n `168`; fx avg `0.0024` n `6`; index avg `-0.0063` n `27`; metal avg `0.0184` n `20`; unknown avg `61.5982` n `1263`
- 1h: commodity avg `0.055` n `13`; crypto_alt avg `-0.5046` n `239`; crypto_major avg `-0.388` n `8`; equity avg `-0.3709` n `168`; fx avg `-0.005` n `6`; index avg `-0.025` n `27`; metal avg `-0.0634` n `20`; unknown avg `50.8937` n `1223`
- 4h: commodity avg `0.03` n `13`; crypto_alt avg `-0.6448` n `239`; crypto_major avg `-0.593` n `8`; equity avg `-0.2255` n `168`; fx avg `0.0061` n `6`; index avg `-0.0135` n `27`; metal avg `-0.0081` n `20`; unknown avg `236.3343` n `1143`
- 24h: commodity avg `0.1049` n `13`; crypto_alt avg `1.1421` n `239`; crypto_major avg `0.5535` n `8`; equity avg `0.7512` n `168`; fx avg `-0.012` n `6`; index avg `0.0706` n `27`; metal avg `-0.0268` n `20`; unknown avg `205.8929` n `993`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
