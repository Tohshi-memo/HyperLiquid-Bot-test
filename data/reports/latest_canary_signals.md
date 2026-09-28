# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T08:07:29.465992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0386` n `12`; crypto_alt avg `0.1317` n `234`; crypto_major avg `0.0406` n `8`; equity avg `0.0059` n `141`; fx avg `-0.0884` n `6`; index avg `-0.0059` n `26`; metal avg `0.0717` n `20`; unknown avg `2.9067` n `944`
- 1h: commodity avg `0.1222` n `12`; crypto_alt avg `-0.9047` n `234`; crypto_major avg `-0.2699` n `8`; equity avg `-0.0898` n `141`; fx avg `-0.0659` n `6`; index avg `-0.015` n `26`; metal avg `0.0346` n `20`; unknown avg `10.8009` n `944`
- 4h: commodity avg `0.0804` n `12`; crypto_alt avg `-1.4976` n `234`; crypto_major avg `-0.7789` n `8`; equity avg `-0.7615` n `141`; fx avg `-0.0349` n `6`; index avg `-0.0566` n `26`; metal avg `-0.2089` n `20`; unknown avg `28.5888` n `920`
- 24h: commodity avg `-0.2224` n `12`; crypto_alt avg `-4.3471` n `234`; crypto_major avg `-3.3539` n `8`; equity avg `-2.3826` n `141`; fx avg `0.0068` n `6`; index avg `-0.2401` n `26`; metal avg `-0.9082` n `20`; unknown avg `6.2204` n `815`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
