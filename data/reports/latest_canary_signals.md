# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T09:37:32.491091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `0.2682` n `234`; crypto_major avg `0.1445` n `8`; equity avg `0.0251` n `141`; fx avg `-0.0045` n `6`; index avg `0.0032` n `26`; metal avg `0.0043` n `20`; unknown avg `0.0434` n `961`
- 1h: commodity avg `0.0219` n `12`; crypto_alt avg `-0.1033` n `234`; crypto_major avg `-0.1826` n `8`; equity avg `0.0054` n `141`; fx avg `0.0001` n `6`; index avg `0.0017` n `26`; metal avg `-0.0` n `20`; unknown avg `0.3269` n `959`
- 4h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.9507` n `234`; crypto_major avg `0.6874` n `8`; equity avg `0.1532` n `141`; fx avg `-0.0166` n `6`; index avg `0.0328` n `26`; metal avg `0.0061` n `20`; unknown avg `4.1055` n `923`
- 24h: commodity avg `0.0587` n `12`; crypto_alt avg `1.6464` n `234`; crypto_major avg `1.0553` n `8`; equity avg `0.4339` n `141`; fx avg `-0.0032` n `6`; index avg `0.036` n `26`; metal avg `-0.0006` n `20`; unknown avg `6.6818` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
