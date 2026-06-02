# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T07:22:20.393236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.76` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.6663` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.1798` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.9124` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1012` n `12`; crypto_alt avg `0.3961` n `228`; crypto_major avg `0.5117` n `8`; equity avg `0.0355` n `69`; fx avg `-0.007` n `6`; index avg `0.0549` n `23`; metal avg `0.0222` n `18`; unknown avg `-0.1539` n `422`
- 1h: commodity avg `0.0565` n `12`; crypto_alt avg `0.1085` n `228`; crypto_major avg `0.0889` n `8`; equity avg `0.0002` n `69`; fx avg `0.02` n `6`; index avg `0.1095` n `23`; metal avg `0.1449` n `18`; unknown avg `-0.0373` n `422`
- 4h: commodity avg `-0.2808` n `12`; crypto_alt avg `-0.9833` n `228`; crypto_major avg `-1.359` n `8`; equity avg `0.8208` n `69`; fx avg `0.0613` n `6`; index avg `0.5534` n `23`; metal avg `1.3073` n `18`; unknown avg `0.1184` n `412`
- 24h: commodity avg `-1.1331` n `12`; crypto_alt avg `-0.3889` n `228`; crypto_major avg `-1.4387` n `8`; equity avg `0.1381` n `69`; fx avg `0.1229` n `6`; index avg `-0.6942` n `23`; metal avg `1.2318` n `18`; unknown avg `1.7461` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.194`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
