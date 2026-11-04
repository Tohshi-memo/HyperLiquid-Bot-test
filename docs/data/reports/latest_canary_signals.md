# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T06:22:24.092812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0474` n `13`; crypto_alt avg `0.1828` n `239`; crypto_major avg `0.0435` n `8`; equity avg `-0.1156` n `158`; fx avg `-0.0021` n `6`; index avg `-0.0174` n `27`; metal avg `0.1662` n `20`; unknown avg `-0.2326` n `1264`
- 1h: commodity avg `0.0127` n `13`; crypto_alt avg `0.9294` n `239`; crypto_major avg `0.4987` n `8`; equity avg `1.2101` n `158`; fx avg `0.0223` n `6`; index avg `0.0971` n `27`; metal avg `0.7394` n `20`; unknown avg `0.1757` n `1242`
- 4h: commodity avg `0.279` n `13`; crypto_alt avg `1.7935` n `239`; crypto_major avg `1.2721` n `8`; equity avg `1.9592` n `158`; fx avg `0.0491` n `6`; index avg `0.2857` n `27`; metal avg `0.861` n `20`; unknown avg `0.4409` n `1238`
- 24h: commodity avg `-0.032` n `13`; crypto_alt avg `2.3439` n `239`; crypto_major avg `1.3868` n `8`; equity avg `2.4985` n `158`; fx avg `0.1357` n `6`; index avg `0.0985` n `27`; metal avg `0.7525` n `20`; unknown avg `190.3005` n `1051`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2023`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
