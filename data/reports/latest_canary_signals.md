# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T01:52:30.776417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0411` n `13`; crypto_alt avg `0.3022` n `237`; crypto_major avg `0.1875` n `8`; equity avg `0.3008` n `151`; fx avg `-0.0009` n `6`; index avg `0.0311` n `26`; metal avg `0.0893` n `20`; unknown avg `1.8956` n `1198`
- 1h: commodity avg `0.0713` n `13`; crypto_alt avg `0.1092` n `237`; crypto_major avg `0.033` n `8`; equity avg `0.3452` n `151`; fx avg `0.0316` n `6`; index avg `0.0692` n `26`; metal avg `0.0057` n `20`; unknown avg `1.7393` n `1196`
- 4h: commodity avg `0.1005` n `13`; crypto_alt avg `0.3711` n `237`; crypto_major avg `-0.0447` n `8`; equity avg `-0.5925` n `151`; fx avg `-0.0311` n `6`; index avg `-0.1162` n `26`; metal avg `-0.1032` n `20`; unknown avg `-0.0597` n `1178`
- 24h: commodity avg `0.1965` n `13`; crypto_alt avg `-0.1942` n `237`; crypto_major avg `-0.4404` n `8`; equity avg `-0.4037` n `151`; fx avg `-0.0371` n `6`; index avg `-0.0342` n `26`; metal avg `-0.3118` n `20`; unknown avg `5.0524` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1983`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
