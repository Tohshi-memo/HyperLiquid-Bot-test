# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T07:37:27.823119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.022` n `12`; crypto_alt avg `-0.1664` n `230`; crypto_major avg `-0.0553` n `8`; equity avg `0.033` n `113`; fx avg `-0.0022` n `6`; index avg `0.0014` n `25`; metal avg `0.0231` n `20`; unknown avg `0.0054` n `786`
- 1h: commodity avg `0.1058` n `12`; crypto_alt avg `-0.1837` n `230`; crypto_major avg `0.1072` n `8`; equity avg `0.2328` n `113`; fx avg `0.0206` n `6`; index avg `0.0074` n `25`; metal avg `0.0755` n `20`; unknown avg `-0.0077` n `786`
- 4h: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.7214` n `230`; crypto_major avg `-0.1444` n `8`; equity avg `0.0673` n `113`; fx avg `0.0077` n `6`; index avg `-0.0105` n `25`; metal avg `0.0552` n `20`; unknown avg `-0.0511` n `770`
- 24h: commodity avg `-0.0408` n `12`; crypto_alt avg `-1.1382` n `230`; crypto_major avg `0.7615` n `8`; equity avg `2.0684` n `113`; fx avg `0.0329` n `6`; index avg `0.1872` n `25`; metal avg `0.2451` n `20`; unknown avg `-0.0636` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2248`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2071`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
