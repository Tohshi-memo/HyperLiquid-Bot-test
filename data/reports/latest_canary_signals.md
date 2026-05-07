# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T00:52:15.969289+00:00`
- Correlation status: `ready`
- Asset price records: `503`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.76` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0568` n `12`; crypto_alt avg `-0.1605` n `228`; crypto_major avg `-0.1375` n `8`; equity avg `0.0002` n `65`; fx avg `0.0115` n `4`; index avg `0.0087` n `23`; metal avg `-0.0734` n `18`; unknown avg `-0.0408` n `356`
- 1h: commodity avg `0.1536` n `12`; crypto_alt avg `-0.6279` n `228`; crypto_major avg `-0.4514` n `8`; equity avg `-0.3549` n `65`; fx avg `0.0662` n `4`; index avg `-0.0368` n `23`; metal avg `-0.1522` n `18`; unknown avg `-0.1238` n `356`
- 4h: commodity avg `0.1369` n `12`; crypto_alt avg `-0.2217` n `228`; crypto_major avg `-0.3833` n `8`; equity avg `-0.2985` n `65`; fx avg `0.0636` n `4`; index avg `0.0132` n `23`; metal avg `0.0088` n `18`; unknown avg `-0.0033` n `356`
- 24h: commodity avg `-1.7801` n `7`; crypto_alt avg `1.7701` n `223`; crypto_major avg `-0.0192` n `7`; equity avg `1.5612` n `47`; fx avg `-0.2538` n `4`; index avg `1.0528` n `6`; metal avg `2.4942` n `7`; unknown avg `3.5127` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `499`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `499`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0782`, n `495`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0704`, n `495`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `495`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0686`, n `495`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0613`, n `495`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.061`, n `499`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0608`, n `499`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0581`, n `495`, weak_sample_signal
