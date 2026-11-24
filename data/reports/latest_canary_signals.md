# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T03:37:26.863628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `0.4026` n `239`; crypto_major avg `0.631` n `8`; equity avg `0.4092` n `166`; fx avg `-0.0026` n `6`; index avg `0.0204` n `27`; metal avg `0.0044` n `20`; unknown avg `190.846` n `1262`
- 1h: commodity avg `0.071` n `13`; crypto_alt avg `-0.4387` n `239`; crypto_major avg `-0.2893` n `8`; equity avg `-0.3349` n `166`; fx avg `0.007` n `6`; index avg `-0.0386` n `27`; metal avg `-0.2246` n `20`; unknown avg `316.8986` n `1260`
- 4h: commodity avg `-0.0739` n `13`; crypto_alt avg `-0.4992` n `239`; crypto_major avg `-0.8202` n `8`; equity avg `-0.2339` n `166`; fx avg `0.0438` n `6`; index avg `0.1359` n `27`; metal avg `-0.2208` n `20`; unknown avg `279.8699` n `1252`
- 24h: commodity avg `-1.1796` n `13`; crypto_alt avg `-0.1366` n `239`; crypto_major avg `-0.6555` n `8`; equity avg `4.5267` n `166`; fx avg `-0.2436` n `6`; index avg `0.5851` n `27`; metal avg `0.0294` n `20`; unknown avg `335.2318` n `1046`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
