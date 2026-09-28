# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T16:37:31.892771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0397` n `12`; crypto_alt avg `0.1592` n `234`; crypto_major avg `0.0794` n `8`; equity avg `0.2124` n `141`; fx avg `-0.0008` n `6`; index avg `0.0242` n `26`; metal avg `0.0524` n `20`; unknown avg `0.3982` n `962`
- 1h: commodity avg `-0.4327` n `12`; crypto_alt avg `1.0449` n `234`; crypto_major avg `0.8806` n `8`; equity avg `0.7977` n `141`; fx avg `-0.0219` n `6`; index avg `0.1301` n `26`; metal avg `0.1267` n `20`; unknown avg `13.219` n `954`
- 4h: commodity avg `-0.3033` n `12`; crypto_alt avg `-0.7011` n `234`; crypto_major avg `0.0455` n `8`; equity avg `-0.4237` n `141`; fx avg `0.0067` n `6`; index avg `-0.0488` n `26`; metal avg `-0.0291` n `20`; unknown avg `68.7591` n `904`
- 24h: commodity avg `-0.3917` n `12`; crypto_alt avg `-2.4868` n `234`; crypto_major avg `-0.9991` n `8`; equity avg `-2.7899` n `141`; fx avg `0.0211` n `6`; index avg `-0.2405` n `26`; metal avg `-0.9504` n `20`; unknown avg `21.1745` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1836`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
