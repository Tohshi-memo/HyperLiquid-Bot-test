# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T02:07:20.000141+00:00`
- Correlation status: `ready`
- Asset price records: `508`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.67` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.5425` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.1088` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1382` n `12`; crypto_alt avg `-0.1908` n `228`; crypto_major avg `-0.1728` n `8`; equity avg `0.0196` n `65`; fx avg `0.0205` n `4`; index avg `-0.0134` n `23`; metal avg `-0.0875` n `18`; unknown avg `-0.2686` n `358`
- 1h: commodity avg `-0.4681` n `12`; crypto_alt avg `-0.0879` n `228`; crypto_major avg `-0.0983` n `8`; equity avg `0.3913` n `65`; fx avg `-0.0276` n `4`; index avg `0.1357` n `23`; metal avg `0.4795` n `18`; unknown avg `-0.0894` n `357`
- 4h: commodity avg `-0.271` n `12`; crypto_alt avg `-1.2056` n `228`; crypto_major avg `-0.9595` n `8`; equity avg `0.2565` n `65`; fx avg `0.0735` n `4`; index avg `0.1493` n `23`; metal avg `0.583` n `18`; unknown avg `-0.3023` n `356`
- 24h: commodity avg `-1.9138` n `7`; crypto_alt avg `0.0235` n `223`; crypto_major avg `-1.0076` n `7`; equity avg `1.6136` n `47`; fx avg `-0.2433` n `4`; index avg `1.06` n `6`; metal avg `2.4189` n `7`; unknown avg `3.1348` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1443`, n `504`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.127`, n `504`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `504`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.077`, n `500`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0697`, n `500`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.069`, n `504`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `500`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0677`, n `500`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `504`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0634`, n `504`, weak_sample_signal
