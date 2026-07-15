# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T21:52:43.962621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `0.0492` n `230`; crypto_major avg `0.0317` n `8`; equity avg `0.0539` n `94`; fx avg `0.0012` n `6`; index avg `0.0027` n `25`; metal avg `0.0015` n `20`; unknown avg `0.2098` n `768`
- 1h: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.0392` n `230`; crypto_major avg `-0.0382` n `8`; equity avg `-0.0561` n `94`; fx avg `0.0156` n `6`; index avg `-0.0139` n `25`; metal avg `-0.0119` n `20`; unknown avg `-0.0248` n `768`
- 4h: commodity avg `0.2279` n `12`; crypto_alt avg `-0.0997` n `230`; crypto_major avg `-0.363` n `8`; equity avg `-0.0121` n `94`; fx avg `0.0078` n `6`; index avg `0.0145` n `25`; metal avg `0.1339` n `20`; unknown avg `-0.21` n `768`
- 24h: commodity avg `0.1592` n `12`; crypto_alt avg `0.4473` n `230`; crypto_major avg `0.6589` n `8`; equity avg `-0.5562` n `93`; fx avg `0.222` n `6`; index avg `-0.1506` n `25`; metal avg `0.1118` n `20`; unknown avg `0.037` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
