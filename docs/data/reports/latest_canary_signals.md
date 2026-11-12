# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T04:52:27.858731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0562` n `13`; crypto_alt avg `0.232` n `239`; crypto_major avg `0.1389` n `8`; equity avg `-0.1594` n `161`; fx avg `0.0056` n `6`; index avg `-0.0228` n `27`; metal avg `0.0085` n `20`; unknown avg `159.6317` n `1260`
- 1h: commodity avg `-0.1136` n `13`; crypto_alt avg `-0.0316` n `239`; crypto_major avg `-0.0403` n `8`; equity avg `-0.2271` n `161`; fx avg `0.0054` n `6`; index avg `-0.0294` n `27`; metal avg `-0.0429` n `20`; unknown avg `0.5744` n `1240`
- 4h: commodity avg `-0.152` n `13`; crypto_alt avg `-0.4995` n `239`; crypto_major avg `-0.5354` n `8`; equity avg `-0.2904` n `161`; fx avg `-0.0849` n `6`; index avg `-0.038` n `27`; metal avg `-0.0343` n `20`; unknown avg `20.3812` n `1236`
- 24h: commodity avg `-0.004` n `13`; crypto_alt avg `-1.8881` n `239`; crypto_major avg `-0.5328` n `8`; equity avg `0.134` n `161`; fx avg `-0.2098` n `6`; index avg `-0.0218` n `27`; metal avg `-0.4458` n `20`; unknown avg `1.0642` n `1127`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
