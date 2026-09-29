# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T03:22:32.041231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.4651` n `234`; crypto_major avg `0.2429` n `8`; equity avg `0.0231` n `141`; fx avg `-0.0108` n `6`; index avg `0.0112` n `26`; metal avg `0.004` n `20`; unknown avg `0.245` n `963`
- 1h: commodity avg `0.0753` n `12`; crypto_alt avg `0.7224` n `234`; crypto_major avg `0.4741` n `8`; equity avg `-0.1812` n `141`; fx avg `-0.0136` n `6`; index avg `-0.0393` n `26`; metal avg `0.014` n `20`; unknown avg `0.1207` n `961`
- 4h: commodity avg `0.1208` n `12`; crypto_alt avg `-1.5891` n `234`; crypto_major avg `-0.71` n `8`; equity avg `-0.5123` n `141`; fx avg `-0.0118` n `6`; index avg `-0.0911` n `26`; metal avg `-0.0167` n `20`; unknown avg `0.5708` n `955`
- 24h: commodity avg `0.1973` n `12`; crypto_alt avg `-3.0409` n `234`; crypto_major avg `-1.3174` n `8`; equity avg `-2.1034` n `141`; fx avg `-0.0604` n `6`; index avg `-0.2029` n `26`; metal avg `-0.4168` n `20`; unknown avg `10.2038` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
