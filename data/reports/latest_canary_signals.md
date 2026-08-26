# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T02:07:27.272392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0639` n `12`; crypto_alt avg `-0.0719` n `231`; crypto_major avg `-0.0999` n `8`; equity avg `-0.0154` n `122`; fx avg `-0.0145` n `6`; index avg `0.0067` n `25`; metal avg `0.0599` n `20`; unknown avg `-0.0371` n `796`
- 1h: commodity avg `-0.0425` n `12`; crypto_alt avg `-0.081` n `231`; crypto_major avg `-0.1555` n `8`; equity avg `-0.1352` n `122`; fx avg `-0.0469` n `6`; index avg `0.0131` n `25`; metal avg `0.1814` n `20`; unknown avg `-0.1091` n `796`
- 4h: commodity avg `-0.1254` n `12`; crypto_alt avg `0.2931` n `231`; crypto_major avg `-0.1121` n `8`; equity avg `-0.692` n `122`; fx avg `-0.0244` n `6`; index avg `-0.1287` n `25`; metal avg `0.1214` n `20`; unknown avg `-0.0521` n `795`
- 24h: commodity avg `-0.9273` n `12`; crypto_alt avg `-2.1982` n `231`; crypto_major avg `-2.1109` n `8`; equity avg `1.1504` n `122`; fx avg `-0.0068` n `6`; index avg `0.1555` n `25`; metal avg `0.24` n `20`; unknown avg `-0.3531` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
