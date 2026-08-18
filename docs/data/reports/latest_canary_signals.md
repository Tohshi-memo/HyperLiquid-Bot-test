# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T13:52:32.466277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0638` n `12`; crypto_alt avg `-0.1007` n `230`; crypto_major avg `-0.0255` n `8`; equity avg `-0.5588` n `114`; fx avg `0.0065` n `6`; index avg `-0.0678` n `25`; metal avg `-0.1091` n `20`; unknown avg `-0.078` n `795`
- 1h: commodity avg `0.0293` n `12`; crypto_alt avg `-0.2085` n `230`; crypto_major avg `-0.2013` n `8`; equity avg `-0.6134` n `114`; fx avg `0.0183` n `6`; index avg `-0.0739` n `25`; metal avg `-0.1672` n `20`; unknown avg `-0.1168` n `795`
- 4h: commodity avg `0.1045` n `12`; crypto_alt avg `-0.0015` n `230`; crypto_major avg `-0.0189` n `8`; equity avg `-0.5034` n `114`; fx avg `0.0303` n `6`; index avg `-0.0331` n `25`; metal avg `-0.0984` n `20`; unknown avg `-0.0315` n `795`
- 24h: commodity avg `0.5707` n `12`; crypto_alt avg `-0.8713` n `230`; crypto_major avg `-0.1252` n `8`; equity avg `-3.1475` n `114`; fx avg `-0.0278` n `6`; index avg `-0.6089` n `25`; metal avg `-0.3825` n `20`; unknown avg `-0.2036` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
