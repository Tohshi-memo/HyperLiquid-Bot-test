# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T01:37:13.327638+00:00`
- Correlation status: `ready`
- Asset price records: `506`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.71` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0497` n `12`; crypto_alt avg `0.3579` n `228`; crypto_major avg `0.1692` n `8`; equity avg `0.0559` n `65`; fx avg `-0.0101` n `4`; index avg `0.0232` n `23`; metal avg `-0.1382` n `18`; unknown avg `1.0112` n `357`
- 1h: commodity avg `-0.1838` n `12`; crypto_alt avg `-0.3563` n `228`; crypto_major avg `-0.2266` n `8`; equity avg `0.0166` n `65`; fx avg `-0.0024` n `4`; index avg `0.0302` n `23`; metal avg `0.3021` n `18`; unknown avg `0.8101` n `356`
- 4h: commodity avg `-0.2274` n `12`; crypto_alt avg `-1.1365` n `228`; crypto_major avg `-0.845` n `8`; equity avg `-0.0276` n `65`; fx avg `0.0779` n `4`; index avg `0.0528` n `23`; metal avg `0.2882` n `18`; unknown avg `0.6906` n `356`
- 24h: commodity avg `-1.8454` n `7`; crypto_alt avg `0.8619` n `223`; crypto_major avg `-0.538` n `7`; equity avg `1.4891` n `47`; fx avg `-0.2787` n `4`; index avg `0.9253` n `6`; metal avg `2.4034` n `7`; unknown avg `4.2506` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1338`, n `502`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `502`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `502`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0705`, n `498`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `502`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.064`, n `502`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.064`, n `498`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0623`, n `498`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0604`, n `498`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0596`, n `498`, weak_sample_signal
