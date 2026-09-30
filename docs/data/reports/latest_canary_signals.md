# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T11:52:28.434828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.1392` n `234`; crypto_major avg `0.0461` n `8`; equity avg `-0.0275` n `142`; fx avg `-0.0038` n `6`; index avg `-0.0324` n `26`; metal avg `-0.0613` n `20`; unknown avg `1.9662` n `963`
- 1h: commodity avg `0.0507` n `12`; crypto_alt avg `-0.0118` n `234`; crypto_major avg `0.0484` n `8`; equity avg `-0.1061` n `142`; fx avg `0.0005` n `6`; index avg `-0.038` n `26`; metal avg `-0.0724` n `20`; unknown avg `1.9391` n `961`
- 4h: commodity avg `0.3849` n `12`; crypto_alt avg `0.7287` n `234`; crypto_major avg `0.7733` n `8`; equity avg `-0.3491` n `142`; fx avg `0.1105` n `6`; index avg `-0.1189` n `26`; metal avg `-0.225` n `20`; unknown avg `2.8281` n `945`
- 24h: commodity avg `-0.0939` n `12`; crypto_alt avg `-0.5587` n `234`; crypto_major avg `-0.6225` n `8`; equity avg `-0.2695` n `142`; fx avg `0.0454` n `6`; index avg `-0.0698` n `26`; metal avg `-0.0504` n `20`; unknown avg `2684.484` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
