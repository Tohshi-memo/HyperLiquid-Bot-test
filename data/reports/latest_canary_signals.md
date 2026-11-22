# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T19:07:28.230859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `0.0878` n `239`; crypto_major avg `-0.0385` n `8`; equity avg `-0.0336` n `166`; fx avg `0.0087` n `6`; index avg `-0.006` n `27`; metal avg `-0.016` n `20`; unknown avg `-0.1689` n `1254`
- 1h: commodity avg `0.0258` n `13`; crypto_alt avg `-0.0431` n `239`; crypto_major avg `0.0395` n `8`; equity avg `-0.2028` n `166`; fx avg `0.0118` n `6`; index avg `-0.0058` n `27`; metal avg `-0.0597` n `20`; unknown avg `159.6381` n `1250`
- 4h: commodity avg `-0.0052` n `13`; crypto_alt avg `-0.1145` n `239`; crypto_major avg `0.0436` n `8`; equity avg `0.0824` n `166`; fx avg `0.0176` n `6`; index avg `0.005` n `27`; metal avg `-0.0253` n `20`; unknown avg `161.8002` n `1229`
- 24h: commodity avg `-0.0736` n `13`; crypto_alt avg `0.6249` n `239`; crypto_major avg `0.5306` n `8`; equity avg `0.9363` n `166`; fx avg `-0.0028` n `6`; index avg `0.1547` n `27`; metal avg `-0.0201` n `20`; unknown avg `244.4526` n `1062`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
