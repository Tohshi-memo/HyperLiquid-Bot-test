# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T13:09:00.856991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1022` n `13`; crypto_alt avg `-0.5268` n `234`; crypto_major avg `-0.3677` n `8`; equity avg `-0.0586` n `142`; fx avg `-0.0008` n `6`; index avg `-0.0078` n `26`; metal avg `-0.076` n `20`; unknown avg `1.0364` n `973`
- 1h: commodity avg `-0.016` n `13`; crypto_alt avg `-0.7711` n `234`; crypto_major avg `-0.7251` n `8`; equity avg `-0.1982` n `142`; fx avg `-0.0285` n `6`; index avg `-0.0353` n `26`; metal avg `-0.0711` n `20`; unknown avg `1.3673` n `973`
- 4h: commodity avg `-0.1895` n `13`; crypto_alt avg `-1.0889` n `234`; crypto_major avg `-0.2387` n `8`; equity avg `-0.1566` n `142`; fx avg `-0.0361` n `6`; index avg `0.0239` n `26`; metal avg `0.2166` n `20`; unknown avg `1.5815` n `967`
- 24h: commodity avg `-0.165` n `13`; crypto_alt avg `-2.762` n `234`; crypto_major avg `-1.7681` n `8`; equity avg `-0.4247` n `142`; fx avg `0.0644` n `6`; index avg `0.0097` n `26`; metal avg `-0.2493` n `20`; unknown avg `779.0365` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
