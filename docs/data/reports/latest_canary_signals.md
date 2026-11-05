# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T06:52:26.797991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.032` n `13`; crypto_alt avg `0.1866` n `239`; crypto_major avg `0.2012` n `8`; equity avg `0.3431` n `158`; fx avg `-0.0158` n `6`; index avg `0.0284` n `27`; metal avg `0.0575` n `20`; unknown avg `0.4353` n `1263`
- 1h: commodity avg `-0.0957` n `13`; crypto_alt avg `0.5668` n `239`; crypto_major avg `0.3578` n `8`; equity avg `0.6376` n `158`; fx avg `-0.0218` n `6`; index avg `0.0656` n `27`; metal avg `0.1517` n `20`; unknown avg `-0.1695` n `1235`
- 4h: commodity avg `-0.0043` n `13`; crypto_alt avg `-0.2574` n `239`; crypto_major avg `-0.1727` n `8`; equity avg `-0.5738` n `158`; fx avg `-0.0097` n `6`; index avg `-0.1531` n `27`; metal avg `-0.1401` n `20`; unknown avg `-0.0634` n `1209`
- 24h: commodity avg `-2.024` n `13`; crypto_alt avg `1.1791` n `239`; crypto_major avg `2.2384` n `8`; equity avg `-2.1845` n `158`; fx avg `0.0499` n `6`; index avg `-0.1069` n `27`; metal avg `0.8541` n `20`; unknown avg `30.7273` n `1008`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2515`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
