# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T20:53:02.478038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `-0.1725` n `230`; crypto_major avg `-0.1738` n `8`; equity avg `-0.0119` n `92`; fx avg `0.0093` n `6`; index avg `-0.0145` n `25`; metal avg `0.0121` n `20`; unknown avg `-0.1269` n `766`
- 1h: commodity avg `0.0853` n `12`; crypto_alt avg `-0.4021` n `230`; crypto_major avg `-0.3959` n `8`; equity avg `-0.1712` n `92`; fx avg `-0.0123` n `6`; index avg `-0.0807` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.2165` n `766`
- 4h: commodity avg `0.4643` n `12`; crypto_alt avg `-0.8371` n `230`; crypto_major avg `-0.4414` n `8`; equity avg `-0.3471` n `92`; fx avg `-0.0226` n `6`; index avg `-0.1144` n `25`; metal avg `0.0228` n `20`; unknown avg `-0.4077` n `766`
- 24h: commodity avg `0.6503` n `12`; crypto_alt avg `-2.5588` n `230`; crypto_major avg `-3.2148` n `8`; equity avg `-3.3472` n `92`; fx avg `-0.0709` n `6`; index avg `-0.6925` n `25`; metal avg `-0.5472` n `20`; unknown avg `-0.3626` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
