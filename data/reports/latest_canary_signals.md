# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T14:52:49.205966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0386` n `13`; crypto_alt avg `0.1393` n `239`; crypto_major avg `0.2033` n `8`; equity avg `0.2809` n `163`; fx avg `0.0108` n `6`; index avg `-0.0052` n `27`; metal avg `-0.0165` n `20`; unknown avg `0.1101` n `1266`
- 1h: commodity avg `-0.2524` n `13`; crypto_alt avg `-0.3707` n `239`; crypto_major avg `-0.4944` n `8`; equity avg `-1.554` n `163`; fx avg `-0.0104` n `6`; index avg `-0.1407` n `27`; metal avg `-0.1671` n `20`; unknown avg `-0.1036` n `1264`
- 4h: commodity avg `0.0799` n `13`; crypto_alt avg `-0.5996` n `239`; crypto_major avg `-1.1173` n `8`; equity avg `-2.1872` n `163`; fx avg `-0.0043` n `6`; index avg `-0.2317` n `27`; metal avg `-0.1637` n `20`; unknown avg `0.1978` n `1258`
- 24h: commodity avg `-0.3375` n `13`; crypto_alt avg `-0.3719` n `239`; crypto_major avg `-0.7527` n `8`; equity avg `-0.8006` n `163`; fx avg `-0.1223` n `6`; index avg `-0.0604` n `27`; metal avg `-1.1846` n `20`; unknown avg `2.6014` n `1137`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
