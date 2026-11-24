# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T05:07:31.691794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `13`; crypto_alt avg `0.223` n `239`; crypto_major avg `0.2139` n `8`; equity avg `0.3539` n `166`; fx avg `-0.0044` n `6`; index avg `0.0349` n `27`; metal avg `0.0453` n `20`; unknown avg `0.8328` n `1260`
- 1h: commodity avg `-0.0407` n `13`; crypto_alt avg `0.676` n `239`; crypto_major avg `0.4547` n `8`; equity avg `0.2636` n `166`; fx avg `-0.0179` n `6`; index avg `0.0181` n `27`; metal avg `0.067` n `20`; unknown avg `0.4681` n `1254`
- 4h: commodity avg `-0.2364` n `13`; crypto_alt avg `0.1134` n `239`; crypto_major avg `-0.5852` n `8`; equity avg `-0.942` n `166`; fx avg `-0.0638` n `6`; index avg `-0.0364` n `27`; metal avg `-0.3749` n `20`; unknown avg `162.4925` n `1238`
- 24h: commodity avg `-1.3219` n `13`; crypto_alt avg `0.9417` n `239`; crypto_major avg `0.4937` n `8`; equity avg `5.2439` n `166`; fx avg `-0.2815` n `6`; index avg `0.7057` n `27`; metal avg `0.0946` n `20`; unknown avg `482.9271` n `1038`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
