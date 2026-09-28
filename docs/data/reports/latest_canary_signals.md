# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T15:37:36.889801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `12`; crypto_alt avg `0.7639` n `234`; crypto_major avg `0.5653` n `8`; equity avg `0.2374` n `141`; fx avg `-0.0125` n `6`; index avg `0.0433` n `26`; metal avg `0.0286` n `20`; unknown avg `1.5417` n `962`
- 1h: commodity avg `0.09` n `12`; crypto_alt avg `-0.2316` n `234`; crypto_major avg `-0.0435` n `8`; equity avg `-0.229` n `141`; fx avg `0.023` n `6`; index avg `-0.049` n `26`; metal avg `-0.0574` n `20`; unknown avg `2.186` n `960`
- 4h: commodity avg `-0.0437` n `12`; crypto_alt avg `-0.7095` n `234`; crypto_major avg `-0.299` n `8`; equity avg `-1.0941` n `141`; fx avg `0.0481` n `6`; index avg `-0.1353` n `26`; metal avg `-0.1715` n `20`; unknown avg `56.3366` n `904`
- 24h: commodity avg `-0.016` n `12`; crypto_alt avg `-2.917` n `234`; crypto_major avg `-1.7831` n `8`; equity avg `-3.5077` n `141`; fx avg `0.0533` n `6`; index avg `-0.355` n `26`; metal avg `-1.0667` n `20`; unknown avg `4.6424` n `786`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2005`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
