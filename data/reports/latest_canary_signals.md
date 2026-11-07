# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T00:22:29.732490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0148` n `13`; crypto_alt avg `0.0559` n `239`; crypto_major avg `0.0963` n `8`; equity avg `-0.0289` n `158`; fx avg `0.0014` n `6`; index avg `-0.0059` n `27`; metal avg `-0.0037` n `20`; unknown avg `0.6471` n `1261`
- 1h: commodity avg `-0.0167` n `13`; crypto_alt avg `0.1679` n `239`; crypto_major avg `0.1952` n `8`; equity avg `0.0041` n `158`; fx avg `-0.0063` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0044` n `20`; unknown avg `2.0175` n `1249`
- 4h: commodity avg `-0.0416` n `13`; crypto_alt avg `-0.3139` n `239`; crypto_major avg `0.2106` n `8`; equity avg `-0.0217` n `158`; fx avg `0.0055` n `6`; index avg `-0.0345` n `27`; metal avg `0.0424` n `20`; unknown avg `19.9298` n `1171`
- 24h: commodity avg `0.1453` n `13`; crypto_alt avg `1.3925` n `239`; crypto_major avg `0.0251` n `8`; equity avg `2.2993` n `158`; fx avg `-0.089` n `6`; index avg `0.3114` n `27`; metal avg `-0.0482` n `20`; unknown avg `8.4788` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
