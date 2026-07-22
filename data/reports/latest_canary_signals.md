# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T11:37:25.640276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0533` n `12`; crypto_alt avg `-0.0911` n `230`; crypto_major avg `-0.1201` n `8`; equity avg `-0.1801` n `98`; fx avg `-0.0003` n `6`; index avg `-0.0249` n `25`; metal avg `-0.0245` n `20`; unknown avg `0.1186` n `773`
- 1h: commodity avg `0.0611` n `12`; crypto_alt avg `-0.0573` n `230`; crypto_major avg `-0.0496` n `8`; equity avg `-0.2777` n `98`; fx avg `-0.0044` n `6`; index avg `-0.0598` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.732` n `773`
- 4h: commodity avg `-0.0425` n `12`; crypto_alt avg `0.6304` n `230`; crypto_major avg `0.6099` n `8`; equity avg `0.0012` n `98`; fx avg `-0.0108` n `6`; index avg `0.0037` n `25`; metal avg `0.0127` n `20`; unknown avg `0.8441` n `772`
- 24h: commodity avg `0.5519` n `12`; crypto_alt avg `-0.5638` n `230`; crypto_major avg `-1.2737` n `8`; equity avg `0.4397` n `98`; fx avg `-0.0123` n `6`; index avg `-0.0482` n `25`; metal avg `0.3536` n `20`; unknown avg `0.8984` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1039`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0829`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0744`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0698`, n `666`, weak_sample_signal
