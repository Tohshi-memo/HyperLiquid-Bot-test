# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T21:52:31.592709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `13`; crypto_alt avg `-0.0214` n `239`; crypto_major avg `-0.0104` n `8`; equity avg `0.1382` n `162`; fx avg `0.0054` n `6`; index avg `0.0488` n `27`; metal avg `0.0689` n `20`; unknown avg `6.54` n `1262`
- 1h: commodity avg `0.1006` n `13`; crypto_alt avg `-0.6028` n `239`; crypto_major avg `-0.9373` n `8`; equity avg `-0.7711` n `162`; fx avg `-0.0078` n `6`; index avg `-0.0506` n `27`; metal avg `-0.0332` n `20`; unknown avg `3.1294` n `1224`
- 4h: commodity avg `0.1709` n `13`; crypto_alt avg `-0.7064` n `239`; crypto_major avg `-0.7475` n `8`; equity avg `-0.0645` n `162`; fx avg `-0.0348` n `6`; index avg `0.0484` n `27`; metal avg `-0.1434` n `20`; unknown avg `2.3512` n `1216`
- 24h: commodity avg `-0.2458` n `13`; crypto_alt avg `-1.2698` n `239`; crypto_major avg `-2.4896` n `8`; equity avg `-2.9829` n `162`; fx avg `-0.0728` n `6`; index avg `-0.2111` n `27`; metal avg `-0.2876` n `20`; unknown avg `0.8965` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
