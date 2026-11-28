# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T17:07:25.540867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `0.3078` n `239`; crypto_major avg `0.2373` n `8`; equity avg `0.0174` n `168`; fx avg `0.0064` n `6`; index avg `-0.0021` n `27`; metal avg `0.0011` n `20`; unknown avg `10.7542` n `1241`
- 1h: commodity avg `-0.0195` n `13`; crypto_alt avg `0.1208` n `239`; crypto_major avg `0.1898` n `8`; equity avg `0.0375` n `168`; fx avg `-0.0032` n `6`; index avg `-0.0016` n `27`; metal avg `0.005` n `20`; unknown avg `11.5536` n `1235`
- 4h: commodity avg `-0.0357` n `13`; crypto_alt avg `-0.6237` n `239`; crypto_major avg `0.2637` n `8`; equity avg `-0.0506` n `168`; fx avg `0.0274` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0237` n `20`; unknown avg `1.8585` n `1221`
- 24h: commodity avg `-0.1196` n `13`; crypto_alt avg `-2.6374` n `239`; crypto_major avg `-0.9527` n `8`; equity avg `0.436` n `168`; fx avg `0.0003` n `6`; index avg `0.0418` n `27`; metal avg `0.2591` n `20`; unknown avg `192.7032` n `1076`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
