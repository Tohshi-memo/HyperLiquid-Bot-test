# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T19:22:46.531370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `13`; crypto_alt avg `-0.0447` n `239`; crypto_major avg `-0.0437` n `8`; equity avg `0.0411` n `162`; fx avg `0.0017` n `6`; index avg `0.0013` n `27`; metal avg `0.0405` n `20`; unknown avg `0.0658` n `1264`
- 1h: commodity avg `-0.1488` n `13`; crypto_alt avg `-0.0214` n `239`; crypto_major avg `-0.0294` n `8`; equity avg `0.2389` n `162`; fx avg `0.0083` n `6`; index avg `-0.0103` n `27`; metal avg `0.1074` n `20`; unknown avg `-0.1277` n `1264`
- 4h: commodity avg `-0.2875` n `13`; crypto_alt avg `0.8062` n `239`; crypto_major avg `0.9079` n `8`; equity avg `-0.0827` n `162`; fx avg `-0.0391` n `6`; index avg `-0.0309` n `27`; metal avg `-0.0118` n `20`; unknown avg `7.8817` n `1237`
- 24h: commodity avg `-1.1313` n `13`; crypto_alt avg `-0.1707` n `239`; crypto_major avg `-0.1389` n `8`; equity avg `-2.8146` n `162`; fx avg `-0.0868` n `6`; index avg `-0.2795` n `27`; metal avg `-0.2285` n `20`; unknown avg `250.733` n `1037`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1364`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1261`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1192`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1032`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1011`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0947`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0885`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `669`, weak_sample_signal
