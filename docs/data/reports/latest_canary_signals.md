# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T19:44:20.367892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0333` n `12`; crypto_alt avg `-0.6504` n `231`; crypto_major avg `-0.7398` n `8`; equity avg `-0.0047` n `122`; fx avg `-0.0075` n `6`; index avg `0.0115` n `25`; metal avg `-0.0181` n `20`; unknown avg `-0.0287` n `795`
- 1h: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.8392` n `231`; crypto_major avg `-0.6544` n `8`; equity avg `-0.1038` n `122`; fx avg `-0.0121` n `6`; index avg `0.0005` n `25`; metal avg `0.0911` n `20`; unknown avg `-0.1285` n `795`
- 4h: commodity avg `0.1224` n `12`; crypto_alt avg `-0.7589` n `231`; crypto_major avg `-0.5794` n `8`; equity avg `-0.1143` n `122`; fx avg `-0.0004` n `6`; index avg `-0.0177` n `25`; metal avg `0.0769` n `20`; unknown avg `-0.2159` n `795`
- 24h: commodity avg `-0.5783` n `12`; crypto_alt avg `-1.2162` n `231`; crypto_major avg `0.0739` n `8`; equity avg `1.7607` n `122`; fx avg `0.0397` n `6`; index avg `0.1886` n `25`; metal avg `0.0311` n `20`; unknown avg `-0.4368` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
