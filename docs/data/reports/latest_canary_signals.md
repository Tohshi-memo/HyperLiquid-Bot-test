# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T09:37:32.784964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `-0.0905` n `234`; crypto_major avg `-0.0917` n `8`; equity avg `-0.0148` n `142`; fx avg `0.0115` n `6`; index avg `0.0013` n `26`; metal avg `0.0126` n `20`; unknown avg `-0.0206` n `985`
- 1h: commodity avg `-0.0496` n `13`; crypto_alt avg `-0.3398` n `234`; crypto_major avg `-0.3565` n `8`; equity avg `-0.0314` n `142`; fx avg `0.0118` n `6`; index avg `0.0008` n `26`; metal avg `-0.0642` n `20`; unknown avg `-0.3184` n `983`
- 4h: commodity avg `-0.6483` n `13`; crypto_alt avg `0.4367` n `234`; crypto_major avg `0.4768` n `8`; equity avg `0.5475` n `142`; fx avg `-0.0821` n `6`; index avg `0.1268` n `26`; metal avg `-0.0473` n `20`; unknown avg `-0.306` n `891`
- 24h: commodity avg `-0.6676` n `13`; crypto_alt avg `1.4168` n `234`; crypto_major avg `1.9068` n `8`; equity avg `1.184` n `142`; fx avg `-0.3379` n `6`; index avg `0.2281` n `26`; metal avg `0.2179` n `20`; unknown avg `-0.1673` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
