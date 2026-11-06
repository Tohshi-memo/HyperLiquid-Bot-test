# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T15:07:29.849547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `-0.1876` n `239`; crypto_major avg `-0.1976` n `8`; equity avg `-0.6533` n `158`; fx avg `-0.0058` n `6`; index avg `-0.0458` n `27`; metal avg `-0.0753` n `20`; unknown avg `0.399` n `1251`
- 1h: commodity avg `-0.1138` n `13`; crypto_alt avg `0.5654` n `239`; crypto_major avg `0.0712` n `8`; equity avg `-0.3751` n `158`; fx avg `0.0201` n `6`; index avg `0.0612` n `27`; metal avg `0.131` n `20`; unknown avg `0.8722` n `1251`
- 4h: commodity avg `-0.2222` n `13`; crypto_alt avg `0.4362` n `239`; crypto_major avg `-0.2755` n `8`; equity avg `-0.1466` n `158`; fx avg `0.0207` n `6`; index avg `0.0733` n `27`; metal avg `0.0021` n `20`; unknown avg `76.428` n `1187`
- 24h: commodity avg `0.1716` n `13`; crypto_alt avg `0.2502` n `239`; crypto_major avg `-2.4424` n `8`; equity avg `-0.3922` n `158`; fx avg `-0.0378` n `6`; index avg `-0.1583` n `27`; metal avg `-0.4392` n `20`; unknown avg `4.0603` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
