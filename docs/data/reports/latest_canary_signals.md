# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T14:37:18.558128+00:00`
- Correlation status: `ready`
- Asset price records: `654`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `-0.0013` n `228`; crypto_major avg `-0.1475` n `8`; equity avg `-0.3891` n `65`; fx avg `0.0026` n `5`; index avg `-0.1654` n `23`; metal avg `-0.0308` n `18`; unknown avg `-0.1199` n `375`
- 1h: commodity avg `0.401` n `12`; crypto_alt avg `0.8067` n `228`; crypto_major avg `0.4392` n `8`; equity avg `0.1142` n `65`; fx avg `0.0212` n `5`; index avg `0.1441` n `23`; metal avg `-0.3513` n `18`; unknown avg `0.0957` n `375`
- 4h: commodity avg `0.3749` n `12`; crypto_alt avg `0.5558` n `228`; crypto_major avg `0.1739` n `8`; equity avg `0.6518` n `65`; fx avg `-0.0424` n `5`; index avg `0.4145` n `23`; metal avg `-0.2668` n `18`; unknown avg `0.0153` n `375`
- 24h: commodity avg `2.0858` n `12`; crypto_alt avg `2.527` n `228`; crypto_major avg `0.0463` n `8`; equity avg `0.374` n `65`; fx avg `0.2433` n `5`; index avg `0.1876` n `23`; metal avg `-0.8354` n `18`; unknown avg `0.0269` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1244`, n `646`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1212`, n `646`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `650`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0978`, n `646`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `646`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `650`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.092`, n `650`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0912`, n `650`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `650`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `650`, weak_sample_signal
