# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T06:37:17.226128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5068` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `-0.4021` n `228`; crypto_major avg `-0.2322` n `8`; equity avg `-0.0822` n `69`; fx avg `-0.0043` n `6`; index avg `-0.024` n `23`; metal avg `-0.0256` n `18`; unknown avg `-0.0882` n `422`
- 1h: commodity avg `0.1911` n `12`; crypto_alt avg `-0.7249` n `228`; crypto_major avg `-0.2729` n `8`; equity avg `-0.0453` n `69`; fx avg `-0.088` n `6`; index avg `0.1323` n `23`; metal avg `-0.1643` n `18`; unknown avg `0.194` n `412`
- 4h: commodity avg `0.279` n `12`; crypto_alt avg `-1.222` n `228`; crypto_major avg `-0.592` n `8`; equity avg `-0.207` n `69`; fx avg `-0.0977` n `6`; index avg `0.9148` n `23`; metal avg `-0.3631` n `18`; unknown avg `0.2006` n `412`
- 24h: commodity avg `1.2372` n `12`; crypto_alt avg `-0.6955` n `228`; crypto_major avg `-1.1085` n `8`; equity avg `0.2243` n `69`; fx avg `-0.0654` n `6`; index avg `0.4792` n `23`; metal avg `0.0959` n `18`; unknown avg `1.5666` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2876`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2263`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
