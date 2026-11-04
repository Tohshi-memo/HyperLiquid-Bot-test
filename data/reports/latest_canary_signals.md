# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T10:07:34.091320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0256` n `13`; crypto_alt avg `0.0815` n `239`; crypto_major avg `-0.0094` n `8`; equity avg `0.154` n `158`; fx avg `-0.0153` n `6`; index avg `0.0251` n `27`; metal avg `0.0093` n `20`; unknown avg `0.9167` n `1260`
- 1h: commodity avg `-0.1247` n `13`; crypto_alt avg `0.1368` n `239`; crypto_major avg `0.1199` n `8`; equity avg `0.7203` n `158`; fx avg `0.016` n `6`; index avg `0.1142` n `27`; metal avg `0.1164` n `20`; unknown avg `10.8314` n `1250`
- 4h: commodity avg `-0.1506` n `13`; crypto_alt avg `0.9416` n `239`; crypto_major avg `0.822` n `8`; equity avg `1.1132` n `158`; fx avg `0.0857` n `6`; index avg `0.2366` n `27`; metal avg `0.3632` n `20`; unknown avg `10.9547` n `1164`
- 24h: commodity avg `-0.2752` n `13`; crypto_alt avg `2.5552` n `239`; crypto_major avg `1.5064` n `8`; equity avg `2.4024` n `158`; fx avg `0.1674` n `6`; index avg `0.2198` n `27`; metal avg `1.101` n `20`; unknown avg `0.9878` n `1057`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2587`, n `668`, moderate_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
