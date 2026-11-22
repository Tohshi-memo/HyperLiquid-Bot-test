# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T18:07:27.287269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `13`; crypto_alt avg `-0.2358` n `239`; crypto_major avg `-0.2121` n `8`; equity avg `0.195` n `166`; fx avg `-0.0063` n `6`; index avg `0.0137` n `27`; metal avg `-0.001` n `20`; unknown avg `41.5381` n `1253`
- 1h: commodity avg `-0.0279` n `13`; crypto_alt avg `-0.258` n `239`; crypto_major avg `-0.204` n `8`; equity avg `0.2429` n `166`; fx avg `-0.0045` n `6`; index avg `0.0213` n `27`; metal avg `0.0049` n `20`; unknown avg `39.9798` n `1255`
- 4h: commodity avg `-0.0562` n `13`; crypto_alt avg `-0.3449` n `239`; crypto_major avg `0.1394` n `8`; equity avg `0.3105` n `166`; fx avg `0.0095` n `6`; index avg `0.0231` n `27`; metal avg `0.0682` n `20`; unknown avg `-0.2604` n `1227`
- 24h: commodity avg `-0.0758` n `13`; crypto_alt avg `0.5698` n `239`; crypto_major avg `0.7078` n `8`; equity avg `1.2047` n `166`; fx avg `0.0022` n `6`; index avg `0.2643` n `27`; metal avg `0.0589` n `20`; unknown avg `279.9414` n `1070`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
